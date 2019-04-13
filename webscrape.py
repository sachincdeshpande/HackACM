from bs4 import BeautifulSoup
import requests
import re
def getNineTenMeals():

	page_link = "http://www.ratemyprofessors.com/ShowRatings.jsp?tid=144099"

	page_response = requests.get(page_link, timeout=5)

	page_content = BeautifulSoup(page_response.content, "html.parser")

	textcontent = []
	breakfastList = []
	lunchList = []
	dinnerList = []
	lateNightList = []

	lateNightHappening = False

	htmlMeals = page_content.find_all("div", attrs={'class': "commentsParagraph"})
	print(htmlMeals)

	for i in range(len(htmlMeals)):
	    textcontent.append(htmlMeals[i].text)
	print(textcontent)

	#------
	htmlMeals = page_content.find_all('td', attrs={'valign': 'top'})
	meals = ''

	for i in range(0, len(htmlMeals)):
		meals = meals + htmlMeals[i].text

	if len(meals) == 0:
		return

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

	for s in textcontent:
	    if s in breakfast and s not in breakfastList:
	        breakfastList.append(s)

	for s in textcontent:
	    if s in lunch and s not in lunchList:
	        lunchList.append(s)

	for s in textcontent:
	    if s in dinner and s not in dinnerList:
	        dinnerList.append(s)

	if lateNightHappening:
	    for s in textcontent:
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



getNineTenMeals()
