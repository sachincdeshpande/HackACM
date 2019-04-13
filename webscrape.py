from bs4 import BeautifulSoup
import requests
import re

def get_teacher_reviews():

	page_link = "http://www.ratemyprofessors.com/ShowRatings.jsp?tid=144099"

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

	print("REVS", teacher_reviews)
	print("ATTS", teacher_attributes)
	"""
		teacher_atts[0] = overall quality
		teacher_atts[1] = % would take again
		teacher_atts[2] = level of difficulty
	"""


	all_reviews = page_content.find_all('td', attrs={'valign': 'top'})
	meals = ''
	

	for i in range(0, len(all_reviews)):
		meals = meals + all_reviews[i].text

	if len(meals) == 0:
		return
	"""
	b = meals.split("Lunch")
	breakfast = b[0]
	l = b[1].split("Dinner")
	lunch = l[0]
	dinner = l[1]
	ln = dinner.split("Late Night")
	if len(ln) > 1:
	    lateNight = ln[1]
	    dinner = ln[0]
	    lateNightHappening = True

	breakfast = re.sub(r'\W+', ' ', breakfast)
	lunch = re.sub(r'\W+', ' ', lunch)
	dinner = re.sub(r'\W+', ' ', dinner)
	if lateNightHappening:
	    lateNight = re.sub(r'\W+', ' ', lateNight)

	for s in teacher_reviews:
	    if s in breakfast and s not in breakfastList:
	        breakfastList.append(s)

	for s in teacher_reviews:
	    if s in lunch and s not in lunchList:
	        lunchList.append(s)

	for s in teacher_reviews:
	    if s in dinner and s not in dinnerList:
	        dinnerList.append(s)

	if lateNightHappening:
	    for s in teacher_reviews:
	        if s in lateNight and s not in lateNightList:
	            lateNightList.append(s)

	bf = open("NineTenbreakfast.txt", "w")
	lun = open("NineTenlunch.txt", "w")
	din = open("NineTendinner.txt", "w")
	if lateNightHappening:
		late = open("NineTenlateNight.txt", "w")

	for i in range(len(breakfastList)):
		if '&' in breakfastList[i]:
			breakfastList[i].replace("&", "and")
		if(i < len(breakfastList) - 1):
			bf.write(breakfastList[i] + ", ")
		else:
			bf.write("and " + breakfastList[i])

	for i in range(len(lunchList)):
		if '&' in lunchList[i]:
			lunchList[i].replace("&", "and")
		if(i < len(lunchList) - 1):
			lun.write(lunchList[i] + ", ")
		else:
			lun.write("and " + lunchList[i])

	for i in range(len(dinnerList)):
		if '&' in dinnerList[i]:
			dinnerList[i].replace("&", "and")
		if(i < len(dinnerList) - 1):
			din.write(dinnerList[i] + ", ")
		else:
			din.write("and " + dinnerList[i])

	if lateNightHappening:
		for i in range(len(lateNightList)):
			if '&' in lateNightList[i]:
				lateNightList[i].replace("&", "and")
			if(i < len(lateNightList) - 1):
				late.write(lateNightList[i] + ", ")
			else:
				late.write("and " + lateNightList[i])

	bf.close()
	lun.close()
	din.close()
	if lateNightHappening:
		late.close()

	if not lateNightHappening:
		filenames = ['NineTenbreakfast.txt', 'NineTenlunch.txt', 'NineTendinner.txt']
	else:
		filenames = ['NineTenbreakfast.txt', 'NineTenlunch.txt', 'NineTendinner.txt', 'NineTenlateNight.txt']
	"""


get_teacher_reviews()
