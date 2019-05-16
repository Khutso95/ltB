

import sys
import re


def getCourse(line):
    """returns course name and the lecturer"""
    l_name, c_name = line.rstrip().split("/")    ##EE1
    return l_name, c_name    #EE2

def getCoursesForLects(lectsfn):
    """for each lecturer the function returns a dictionary list of courses"""	
    courses = {}  # dictionary: for each lect returns list of courses
    lf = open(lectsfn)
    for line in lf:
        lect, course = getCourse(line)
        if lect in courses: # is the lecturer in the dictionary
            courses[lect].append(courses)  # add course to the list ##EE3
        else:
            courses[lect] = [course]  
    lf.close()
    return courses

def getExams(examfname):
	"""input an exam name and the fuction returns date of the exam and the vanue """
	exams = {}
	for line in open(examfname):
		data = line.rstrip().split(",")
		exams[data[0]]=(data[1],data[2])
		return exams

def getTimeTable(courses,exams):
	"""this fuction returns a list of exams for each lecturer"""
	ttable = []  # nested list -- for each lect a list of exams
	for lect in sorted(courses.keys()):
		l_exams   = [] # build list of lecturer's exams
		l_courses = courses[lect] # get their courses
		for c in l_courses:
			if c not in exams:
				the_exam=("TBD","TBD")
			else:
				the_exam = exams[c]
			l_exams.append((c,the_exam))
		ttable.append((lect,l_exams)) # now we know the exams add it list
	return ttable

def showTimeTable(ttabsle):
	"""prints the timetable"""
	for (lect, l_exams) in ttable:
		print(lect)
		for c,ex in l_exams:
			print("   ",c,ex[0],ex[1])
        

if __name__ == "__main__":
    examfn    = sys.argv[1]
    lectsfn     = sys.argv[2]
    courses    = getCoursesForLects(lectsfn)
    exams     = getExams(examfn)
    tt = getTimeTable(courses,exams)
    showTimeTable(tt)
