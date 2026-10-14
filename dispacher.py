from check2.characterCheck2 import check2Char
from chracter import charaInfo
from dialogues import dialogueProcessor
#from images import  img
def dispatcher(code):
	if code[0]=="character" and len(code)>=4:
		print("hello charaxtet")
		check2Char(code)
	if code[0] in charaInfo.aliases:
		print("dialogue")
		dialogueProcessor(code)
	if code[0]=="show":
		 print("show")
		 #img(code)