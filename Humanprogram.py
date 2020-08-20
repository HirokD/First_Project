import pyttsx3
import os


pyttsx3.speak("Welcome to my Application")
pyttsx3.speak("HI Sir, How are you")

while True:
	print("How May I Help You Sir : " , end='')
	p = input()
	
	

	if (("run" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and (("chrome" in p) or ("browser" in p)):
 		

		if (("no" in p) or ("dont" in p) or ("don't" in p)) and (("chrome" in p) or ("browser" in p)):
            		 print("Anything Else sir : ",end="\n")
		else:
            		 print("opening Chrome for you.... ",end="\n")
            		 os.system("chrome")
            

	elif (("run" in p) or ("open" in p) or ("launch" in p) or ("start" in p)) and (("notepad" in p) or ("editor" in p)):
 		
		if (("no" in p) or ("dont" in p) or ("don't" in p)) and (("notepad" in p) or ("editor" in p)):
			print("Anything Else sir : ",end="\n")
		else:
			print("opening Notepad for you.... ",end="\n")
			os.system("notepad")

	elif (("run" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and (("player" in p) or ("media" in p) or ("windows" in p)):
 		os.system("wmplayer")
	
	elif (("run" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and (("excel" in p) or ("microsoft" in p) or ("ms excel" in p)):
		os.system("excel")

	elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("player" in p) or ("media" in p) or ("KMPlayer" in p)):
 		os.system("KMPlayer")

	elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("google drive" in p) or ("drive" in p) or ("backup" in p)):
 		os.system("OneDrive")
	
	elif (("play" in p) or ("launch" in p) or ("start" in p)) and (("player" in p) or ("video" in p) or ("song" in p)):
 		os.system("chrome https://www.youtube.com/watch?v=osdoLjUNFnA")
	
	elif (("play" in p) or ("start" in p) or ("launch" in p)) and (("another" in p) or ("next" in p)):
 		os.system("chrome https://www.youtube.com/watch?v=09R8_2nJtjg")

	elif (("run" in p) or ("open" in p)) and ("date" in p):
 		os.system("date")

	elif ("exit" in p) or ("quit" in p) or ("close" in p) or ("shut" in p):
		break
	else:
 		pyttsx3.speak("I'm sorry, I can't find that. Try again please.")
