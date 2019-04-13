from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
import string



test_text = ['Professor Tantalo is a great professor, I really appreciate how he always shows us an example similar to our projects so we get a basic understanding of the programming and lab assignments before we start them. His midterms and finals were also pretty easy and very similar to the review (some exactly off the review).', 'Tantalo explained every topic well, using both drawings and actual code to make sure we all understood everything. There was lots of homework, but it was all doable. The midterm and final were almost identical to the review problems, so they were pretty easy. Overall, a very good class.', "The grade was based on 7 labs (10% grade), 5 projects (20% grade), two mid terms (20% each), and a final( 30% grade). Most of his labs are straight forward and informative. A couple of his project assignments are difficult but he gives many due date extensions. Mid terms and final are similar to the review sheets so study them and u'll be chilling.", "I had to give this class a 1 difficulty because 0 wasn't an option. Understanding ligamas is literally 75% of the class. Programming assignments were as simple as a hello world program. That is in python... In other terms, if this class was instantiated into an object, all of its features would be set to easy.", 'Patrick is a great lecturer who surveys a lot of material in a short amount of time. Attend class and hopefully MSI and everything will go well.', "For 101, the PA's were simple, and if you've taken 12B with him they are even easier. The main work is just memorizing all the proof's he gives you for the midterms and final. Always pushes back assignments. Doesn't curve but you don't need it if you put a good amount of studying in.", "Pretty clear professor, though a bit on the easy side. If you've taken one of his classes, you'll know exactly how they go. 2 midterms and a final, all of which draw heavily from the review problems/homework sets. Programming assignments are really, really easy. Took him for 12A, 12B, 101, got A's each time. Might take him for 201. Good professor.", "Tantalo is a great professor who gives lots of materials to get students started on the assignments. The assignments still aren't all easy, but he makes sure you understand how to do them and what they are. Also he almost always extends every assignment by a week. Straightforward exams and class. Great professor.", "Tantalo was easy to understand. First 3 assignments are easy. pa4 takes a lot of time, definitely get started ASAP on that one. pa5 is slightly challenging if you're new to C. lectures are clear, worth going to. midterms were almost the same as the review. threw a curveball for the final but still did ok", 'I took CMPS 5J, CMPS 11, CMPS 5P, CMPS 12B/M and CMPS 101 with Tantalo and I absolutely loved him. His lectures may be boring, but he is excellent at teaching the concepts. The programming assignments, midterms, and finals are straightforward and I recommend taking as many courses as you can with him.', "The tests are insanely easy: his final was only an hour and a half instead of three hours, and people were turning it in at the 20 minute mark. The programming assignments are also very easy, and you'll get extensions of anywhere from a day to a week on them. That being said, the grading scripts for the programming assignments are impossible.", 'Good professor, lecture kind of boring but the test is very straightforward. Always give the extension for the homework assignment.', "Class was easier than I thought it would be. Tests are surprisingly easy. Programming assignments were interesting and not too difficult. Lecture sometimes is boring and irrelevant. Class didn't feel very coherent. Homework was difficult, and didn't really relate to tests. He's a decent lecturer. The TA's took a long time to return assignments.", "He's one of the few professors I've ever had who can explain concepts both clearly AND with mathematical rigor. I highly recommend you take as many classes with him as you can for the optimal experience as a CS student.", "I've taken mostly all of my CMPS classes from him. He does a good job at explaining everything. The lectures are good and he posts videos and slides online. Very helpful at office hours. The midterm and final is basically the same as the review test but with a few minor changes.", 'I will definitely recommend taking CMPS 101 with him.', 'Great intro class. Tests are similar to practice. Go to lecture. His office hours are helpful.', "Extends every assignment. He's really good.", 'Tantalo is the boy. Never took a computer science class before, but he explains everything in detail in class. He extended every single one of our assignments, so you have more than enough time to finish your work. Final was an exact replica of the study guide.', 'GET HIM! Professor Tantalo is the best CS professor at UCSC. He genuinely cares about students and is very clear at lectures. I never had programming experience before and still did great, but I did go to MSI for help. Last 3 programming assignments are tough but doable. Midterm and Final were similar to the review and was not too hard. Thumbs up.']



def main():
    sent, toks = tokenize_content(test_text)
    sentence_ranks = score_tokens(toks, sent)

    print(sent)
    print(toks)
    print(sentence_ranks)

    print(summarize(sentence_ranks,sent, 4))


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
    (main())