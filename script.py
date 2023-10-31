def extract(s):
	l = s.split(" ")
	o = []
	for e in l:
		email = e.replace("<","").replace(">","")
		if "@" in email and email not in o:
			o.append(email)
	for i in o:
		print(i)
