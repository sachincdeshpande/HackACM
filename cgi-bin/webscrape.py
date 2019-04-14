#!/usr/bin/env

from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
from flask import Flask
import re, requests, json, math, string



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/first-name/last-name")
def run():
    return "Hello World!"

path = "file:///C:/Users/sachi/Desktop/Past%20Classes/CMPS143/HackACM/cgi-bin/webscrape.py"

class RateMyProfScraper:
        def __init__(self,schoolid):
            self.UniversityId = schoolid
            self.professorlist = self.createprofessorlist()
            self.indexnumber = False

        def createprofessorlist(self):#creates List object that include basic information on all Professors from the IDed University
            tempprofessorlist = []
            num_of_prof = self.GetNumOfProfessors(self.UniversityId)
            num_of_pages = math.ceil(num_of_prof / 20)
            i = 1
            while (i <= num_of_pages):# the loop insert all professor into list
                page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=" + str(
                    i) + "&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                    self.UniversityId))
                temp_jsonpage = json.loads(page.content)
                temp_list = temp_jsonpage['professors']
                tempprofessorlist.extend(temp_list)
                i += 1
            return tempprofessorlist

        def GetNumOfProfessors(self,id):  # function returns the number of professors in the university of the given ID.
            page = requests.get(
                "http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                    id))  # get request for page
            temp_jsonpage = json.loads(page.content)
            num_of_prof = temp_jsonpage[
                              'remaining'] + 20  # get the number of professors at William Paterson University
            return num_of_prof

        def SearchProfessor(self, ProfessorName):
            self.indexnumber = self.GetProfessorIndex(ProfessorName)
            self.PrintProfessorInfo()
            return self.indexnumber

        def GetProfessorIndex(self,ProfessorName):  # function searches for professor in list
            for i in range(0, len(self.professorlist)):
                if (ProfessorName == (self.professorlist[i]['tFname'] + " " + self.professorlist[i]['tLname'])):
                    return i
            return False  # Return False is not found

        def PrintProfessorInfo(self):  # print search professor's name and RMP score
            if self.indexnumber == False:
                print("error")
            else:
                print(self.professorlist[self.indexnumber])

        def PrintProfessorDetail(self,key):  # print search professor's name and RMP score
            if self.indexnumber == False:
                print("error")
                return "error"
            else:
                print(self.professorlist[self.indexnumber][key])
                return self.professorlist[self.indexnumber][key]

def get_teacher_reviews(professor_id):

    url = "http://www.ratemyprofessors.com/ShowRatings.jsp?tid=" + str(professor_id)

    page_link = url

    page_response = requests.get(page_link, timeout=5)

    page_content = BeautifulSoup(page_response.content, "html.parser")

    # list used to hold the reviews of a teacher
    teacher_reviews = []
    # list to hold calculated elements on ratemyprofessor
    """
            teacher_atts[0] = overall quality
            teacher_atts[1] = % would take again
            teacher_atts[2] = level of difficulty
    """
    teacher_attributes = []

    # find reviews and teacher attributes on page
    all_reviews = page_content.find_all("p", attrs={'class': "commentsParagraph"})
    attributes = page_content.find_all("div", attrs={'class': "grade"})

    for i in range(len(all_reviews)):
        teacher_reviews.append(all_reviews[i].text)

    for i in range(len(attributes)):
        teacher_attributes.append(attributes[i].text)

    # get rid of unnecessary spaces in  (newline, etc)
    for i in range(0, len(teacher_reviews)):
        current_review = teacher_reviews[i]
        review_no_front_space = re.sub(r'^\W*', '', current_review)
        review_no_space = re.sub(r'\s*$', '', review_no_front_space)
        teacher_reviews[i] = review_no_space

    # get rid of unnecessary spaces in teacher_attributes (newline, etc)
    for i in range(0, len(teacher_attributes)):
        current_attribute = teacher_attributes[i]
        attribute_no_front_space = re.sub(r'^\W*', '', current_attribute)
        attribute_no_space = re.sub(r'\s*$', '', attribute_no_front_space)
        teacher_attributes[i] = attribute_no_space

    return teacher_reviews


def main():
    UCSC_professor_db = RateMyProfScraper(1078)
    UCSC_professor_db.SearchProfessor("Patrick Tantalo")#searchterm) # will be supplied by website
    test_text = get_teacher_reviews(UCSC_professor_db.PrintProfessorDetail("tid"))

    #
    sentences, tokens = tokenize_content(test_text)
    sentence_ranks = score_tokens(tokens, sentences)

    print(summarize(sentence_ranks, sentences, 4))

def tokenize_content(teacher_reviews):
    stop_words = set(stopwords.words('english') + list(punctuation))
    tokens_in_teacher_reviews = []
    sentences = []
    for sentence in teacher_reviews:
        sentences.append(sentence)
        sentence_tokenized = word_tokenize(sentence)
        for word in sentence_tokenized:
            if word.lower() not in stop_words:
                tokens_in_teacher_reviews.append(word)
    return sentences, tokens_in_teacher_reviews


def score_tokens(filt_toks, sentences):

    word_freq = FreqDist(filt_toks)

    ranking = defaultdict(int)
    i = 0

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                ranking[i] += word_freq[word]
        i += 1
    return ranking


def summarize(ranks, sentences, length):

    indexes = nlargest(length, ranks, key=ranks.get)
    final_sentences = [sentences[j] for j in sorted(indexes)]

    return ' '.join(final_sentences)


if __name__ == "__main__":
    main()