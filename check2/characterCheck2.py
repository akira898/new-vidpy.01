from chracter import character

def check2Char(code):
	if len(code)>=4 and code[2]=="as":
		character(code)
		print("acepted")
	elif len(code)<4:
		print("the command character must have at least 4 statements")
	else:
		print("it doent include as")