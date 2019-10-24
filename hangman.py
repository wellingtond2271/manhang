from random import choice
myWord = choice(["howdy" , "hello" , "greetings" , "hi" , "hola", "bonjour", "ola", "hallo", "hej", "tere", "ciao", "ahoj", "kaixo", "bok", "hei", "halla", "bongu", "salut", "komentari", "merhaba", "helo", "salve" ])

Correct = ()
Incorrect = ()

tries = int(input(" Insert the amount of tries you would like sir/madam "))

while tries > 0:
	
	show = ""
	for you in myWord:
		if you guessed:
			show = show + you

		else:
			show = show + "_ "

	if show == myWord:
		break


print("Correct now the word is: " + show)
print(tries "Tries left ")
print("here are your incorrect guesses ")
print(Incorrect)

if Letter in myWord:
	print(" This letter is not in the word")
	guess