import re

for x in range(30):
	testerString = open("output."+(x+1)+".txt")
	for string in testerString:
		if ("S&P" or "STANDARD & POOR") in string:
			m = re.findall('\"([A-D][A-D]?[A-D][-+]?)\"', string)
		if m != None:
			for match in m:
				print match


