commands=["character","show"]
from dispacher import dispatcher
def check1(code):
	badCommand=False
	global commands
	for i in code:
		codeGame=code[i].split()
		print(codeGame)
		if not codeGame:
			continue
		if not codeGame[0]in commands:
			badCommand=True
			break
		else:
			dispatcher(codeGame)
			print("valid")
			
	if badCommand:
			print("this script is not valid")
			return False
	return True