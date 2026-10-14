class dialInGame:
	def __init__(self,dialogues,dialogue,dialogueIn):
		self.dialogues=dialogues
		self.dialogue=dialogue
		self.dialogueIn=dialogueIn
speach=dialInGame({},"",0)
def dialogueProcessor(code):
	#guardo el texto y el alias
	speach.dialogue=" ".join(code[1:])
	speach.dialogues[speach.dialogueIn]=speach.dialogue,code[0]
	print(speach.dialogues)
	speach.dialogueIn+=1
	print(speach.dialogue)
dialogueProcessor("e: helli")