import re

for x in range(6):
	testerString = open("output."+str(x+1)+".txt")
	filename = "output."+str(x+1)+".txt"
	for string in testerString:
		if ("S&P" or "STANDARD & POOR") in string:
		#	string = string.replace(u'\xe2', '\"')	
			m = re.findall('\"([A-D][A-D]?[A-D]?[-+]?)\"', string)
			if m != None:
				for match in m:
					print filename+": " + match


