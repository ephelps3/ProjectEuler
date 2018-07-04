#!/bin/python

from datetime import datetime
import os
import re
import mmap

import unittest
import Problem3
import Problem4
import Problem5
import Problem6
import Problem7
import Problem8
import Problem9
import Problem10
import Problem11
import Problem12
import Problem13
import Problem14

class MyTest(unittest.TestCase):
    def testProblem3(self):
	tick=datetime.now()
        result = self.assertEqual(Problem3.Problem3(), 6857)
	tock=datetime.now()
	diff = tock - tick
	if result == None:
		checkHighscores("Problem3", diff.total_seconds())
    def testProblem4(self):
	tick=datetime.now()
        result = self.assertEqual(Problem4.Problem4(), 906609)
	tock=datetime.now()
	diff = tock - tick
	print(result)
	if result == None:
		checkHighscores("Problem4", diff.total_seconds())
    def testProblem5(self):
	tick=datetime.now()
        result = self.assertEqual(Problem5.Problem5(), 232792560)
	tock=datetime.now()
	diff = tock - tick
	if result == None:
		checkHighscores("Problem5", diff.total_seconds())
    def testProblem6(self):
	tick=datetime.now()
        result = self.assertEqual(Problem6.Problem6(), 25164150)
	tock=datetime.now()
	diff = tock - tick
	if result == None:
		checkHighscores("Problem6", diff.total_seconds())
    def testProblem7(self):
	tick=datetime.now()
        result = self.assertEqual(Problem7.Problem7(), 104743)
	tock=datetime.now()
	diff = tock - tick
	if result == None: 
		checkHighscores("Problem7", diff.total_seconds())
    def testProblem8(self):
	tick=datetime.now()
        result = self.assertEqual(Problem8.Problem8(), 23514624000)
	tock=datetime.now()
	diff = tock - tick
	if result == None:
		checkHighscores("Problem8", diff.total_seconds())
    def testProblem9(self):
	tick=datetime.now()
        result = self.assertEqual(Problem9.Problem9(), 31875000)
	tock=datetime.now()
	diff = tock - tick
	if result == None:
		checkHighscores("Problem9", diff.total_seconds())
    def testProblem12(self):
	tick=datetime.now()
        result = self.assertEqual(Problem12.Problem12(), 76576500)
	tock=datetime.now()
	diff = tock - tick
	if result == None:
		checkHighscores("Problem12", diff.total_seconds())
    def testProblem13(self):
	tick=datetime.now()
        result = self.assertEqual(Problem13.Problem13(), 5537376230)
	tock=datetime.now()
	diff = tock - tick
	if result == None:
		checkHighscores("Problem13", diff.total_seconds())
    def testProblem14(self):
	tick=datetime.now()
        result = self.assertEqual(Problem14.Problem14(), 837799)
	tock=datetime.now()
	diff = tock - tick
	if result == None:
		checkHighscores("Problem14", diff.total_seconds())

def checkHighscores( problem, time):
    print("CHECKING HIGHSCORES...")
    newLines=[]
    with  open("Highscores.txt", "r+") as f:
	lines = f.readlines()
	data = mmap.mmap(f.fileno(), 0)
	mo = re.search(problem, data)
	if not mo:
	    newLines.append("{}:{}\n".format(problem, time))
	for line in lines:
            currentLine = line.split(":")
  	    if  problem in currentLine[0]:
	        currentHigh = float(currentLine[1])
		if currentHigh > time:
		    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
		    print("N E W  H I G H S C O R E!")
		    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
		    print("\n{} beats the old score of {} for {}!".format(time, currentHigh, problem))
		    line = "{}:{}\n".format(problem, time)
	    	    newLines.append(line)
		else:
	    	    newLines.append(line)
	    else:
	        newLines.append(line)
	
    os.remove("Highscores.txt")
    with open("Highscores.txt", "w") as n:
    	for line in newLines:
            n.write(line)

if __name__ == "__main__":
	unittest.main()
