#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def rep_quotes(string):
	string = string.decode("utf-8")
        string = string.replace(u'\u201c', '\"')
        string = string.replace(u'\u201d', '\"')
        string = string.replace(u'\u2018\u2018', '\"')
        string = string.replace(u'\u2019\u2019', '\"')
	return string

for x in range(7):
	testerString = open("output."+str(x+1)+".txt")
	filename = "output."+str(x+1)+".txt" 
	res_count = 0
	for string in testerString:
		if ("S&P" or "STANDARD & POOR" or "Standard & Poor") in string:
			string = rep_quotes(string)
			m = re.findall('\"([A-D][A-D]?[A-D]?[-+]?)\"', string)
			if m != None:
				for match in m:
					print filename+": " + "S&P " + match
				res_count += 1
				if res_count >= 2:
					break
		if ("Moody") in string:
			string = rep_quotes(string)
                        m = re.findall('\"([A-D][a]?[a1-3]?[1-3]?)\"', string)
                        if m != None:
                                for match in m:
                                        print filename+": " + "Moody\'s " + match
                                res_count += 1
                                if res_count >= 2:
                                        break
	print "\n"


