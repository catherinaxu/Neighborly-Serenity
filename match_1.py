import re

testerString = open("output.1.txt")
for string in testerString:
	if "S&P" in string:
		m = re.findall('\"([A-D][A-D]?[A-D][-+]?)\"', string)
	if m != None:
		for match in m:
			print match


