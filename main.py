import random, time, copy #importerar dessa paket
from os import system #till clear screen

#introduktion när spelet startar
print('Welcome to MineSweeper!')

# runs every time we want a new game, resets all the variables, printar main menu.
def reset():
	print('''
MAIN MENU
=========

-> for instructions type 'I'
-> to play type 'P'
''')

	#input, tar in ett värde och gör det till stor bokstav.
	choice = input('''
	Type here:''').upper()

	if choice == 'I': #om man väljer instruktioner
		_ = system('cls') #clear screen

		print(open('instructions.txt', 'r').read())
		input('Press [Enter] when ready to play.')

	elif choice != 'P': #om man inte trycker P eller I
		_ = system('cls') #clear screen
		reset()

	#The solution grid. this contains the locations of all the bombs and numbered cells.
	# en list-array som innehåller 10 lists som innehåller 9 tal vardera.
	b = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

	# för att lägga till bomber på random ställen. anropar funktionen "placebomb" 10 ggr
	for n in range (0, 10):
		placeBomb(b)

	#ändra så att alla 0:or runt omkring en bomb får rätt nummer.
	#add 1 to the numbers in all of the squares surrounding each bomb. This will lead to all of the numbers correctly reflecting the number of bombs surrounding them.
	for r in range (0,9): #loopar genom alla rader och kolumner med dessa 2 for-loops
		for c in range (0,9):
			value = l(r, c, b) # l är location, gets the value in the solution grid at the given coordinates (r and c)
			if value == '*': #om det är en bomb, anropa funktionen "updatevalues"
				updateValues(r, c, b)

	printBoard(b) #printar ut grid:en

#Returnerar värdet på en given kordinat, ger info om bomb osv
def l(r, c, b):
    return b[r][c] #rad och kolumn, returnerar värdet


#funktion som lägger till bomber
def placeBomb(b):
	r = random.randint(0,8) #rad
	c = random.randint(0,8) #kolumn

	#kollar om det redan är en bomb på den random platsen, om inte sätter den en bomb där.
	currentRow = b[r]
	if not currentRow[c] == '*':
		currentRow[c] = '*'
	else:
		placeBomb(b) #om platsen redan är upptagen körs funktionen om.


# funktionen uppdaterar nummer runt en bomb
def updateValues(rn, c, b):

	#Row above.
    if rn-1 > -1:
        r = b[rn-1]
        
        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1

    #Same row.    
    r = b[rn]

    if c-1 > -1:
        if not r[c-1] == '*':
            r[c-1] += 1

    if 9 > c+1:
        if not r[c+1] == '*':
            r[c+1] += 1

    #Row below.
    if 9 > rn+1:
        r = b[rn+1]

        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1


# printar ut griden så spelaren kan sen den
def printBoard(b):
	# rensar skärmen så griden kan printas på nytt
	_ = system('cls') #clear screen

	#print grid, första delen ändras inte
	print('    A   B   C   D   E   F   G   H   I')
	print('  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')

	#denna del uppdateras utefter hur spelaren har spelat
	#hämtar rutornas värde genom funktionen "l(r, c, b)"
	for r in range (0, 9):
		print(r,'║',l(r,0,b),'║',l(r,1,b),'║',l(r,2,b),'║',l(r,3,b),'║',l(r,4,b),'║',l(r,5,b),'║',l(r,6,b),'║',l(r,7,b),'║',l(r,8,b),'║')
		if not r == 8:
			print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
	print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝') # printar sista raden


reset() # ta bort sen