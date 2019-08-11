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
	b = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0]]

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

	#The known grid. Sets the variable k to a grid of blank spaces, because nothing is yet known about the grid.
	k = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

	printBoard(k) #printar ut grid:en (known grid)

	#Startar en timer
	startTime = time.time()

	#Starta spelet!
	play(b, k, startTime)

#Returnerar värdet på en given kordinat, ger info om bomb osv
def l(r, c, b):
    return b[r][c] #rad och kolumn, returnerar värdet

#funktion som lägger till minor
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


#Places a marker in the given location.
def marker(r, c, k):
	k[r][c] = '⚐' # ändrar värdet på kordinaten till en flagga
	printBoard(k) # printar ut known grid igen

# spelaren väljer en kordinat (location)
def choose(b, k, startTime):
	# används för att se att användaren har knappat in giltiga kordinater
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
	# en evighetsloop, den fortsätter även om ogiltiga kordinater har knappats in
	while True:
		chosen = input('Choose a square (eg. E4) or place a marker (eg. mE4): ').lower()

		# kollar efter en giltig ruta, kollar m, nummer, bokstäver och jämför med de 2 arrayerna här ovanför.
		# om man vill lägga en flagga
		if len(chosen) == 3 and chosen[0] == 'm' and chosen[1] in letters and chosen[2] in numbers:
			c, r = (ord(chosen[1]))-97, int(chosen[2]) # ord = returns the ASCII value 
			marker(r, c, k) #sätter en flagga in known grid i rätt kordinater
			play(b, k, startTime) # går tillbaka till spelet
			break 
		# om man vill öppna en ruta, returnerar kordinaten till play
		elif len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers: 
			return (ord(chosen[0]))-97, int(chosen[1])
		# om man skrivit fel så loopas bara frågan.
		else: choose(b, k, startTime)

#När en 0:a hittas i en ruta så öppnas alla 0:or runt den upp.
def zeroProcedure(r, c, k, b):

    #Row above
    if r-1 > -1:
        row = k[r-1]
        if c-1 > -1: row[c-1] = l(r-1, c-1, b)
        row[c] = l(r-1, c, b)
        if 9 > c+1: row[c+1] = l(r-1, c+1, b)

    #Same row
    row = k[r]
    if c-1 > -1: row[c-1] = l(r, c-1, b)
    if 9 > c+1: row[c+1] = l(r, c+1, b)

    #Row below
    if 9 > r+1:
        row = k[r+1]
        if c-1 > -1: row[c-1] = l(r+1, c-1, b)
        row[c] = l(r+1, c, b)
        if 9 > c+1: row[c+1] = l(r+1, c+1, b)


# om värdet är 0 öppnas alla närliggande rutor med 0:or
def checkZeros(k, b, r, c):
	oldGrid = copy.deepcopy(k) #gör en kopia av known grid (k)
	zeroProcedure(r, c, k, b) # kör funktionen "zeroprocedure" som öppnar rutorna
	if oldGrid == k: # kollar om oldgrid är samma som known grid, isåfall har inget ändrats och det är färdigt.
		return # återgår till play

	while True: # loopar genom varje ruta i known grid, öppnar upp rutor i known grid
		oldGrid = copy.deepcopy(k)
		for x in range (9):
			for y in range (9):
				if l(x, y, k) == 0:
					zeroProcedure(x, y, k, b)
		if oldGrid == k: # kollar om oldgrid är samma som known grid, isåfall har inget ändrats och det är färdigt.
			return # återgår till play


# startar spelet
def play(b, k, startTime): # tar in solutiongrid, knowngrid och tid
	c, r = choose(b, k, startTime) # splearen väljer en ruta
	v = l(r, c, b) #hämtar värdet i den rutan

	#om värdet i rutan är en mina så har man förlorat spelet.
	if v == '*':
		printBoard(b) #printar solutiongrid
		print('You Lose!')
		print('Time: ' + str(round(time.time() - startTime)) + 's') #printar ut tiden, nutid-starttid
		playAgain = input('Play again? (Y/N): ').lower() # spela igen?
		if playAgain == 'y':
			_ = system('cls') #clear screen	
			reset()
		else:
			quit()

	#om det inte var en mina i rutan, sätter det värdet i known grid (k)
	k[r][c] = v

	#Om värdet var 0 anropas en funktion som öppnar upp alla närliggande rutor med 0:or.
	if v == 0:
		checkZeros(k, b, r, c)

	printBoard(k) #printar ut grid:en igen

	#Kollar om spelaren har vunnit, räknar ut antalet rutor som finns kvar, 10 rutor = vinst
	squaresLeft = 0
	for x in range (0, 9):
		row = k[x]
		squaresLeft += row.count(' ')
		squaresLeft += row.count('⚐')

	#vid vinst
	if squaresLeft == 10:
		printBoard(b)
		print('You win!')
		print('Time: ' + str(round(time.time() - startTime)) + 's')
		playAgain = input('Play again? (Y/N): ')
		playAgain = playAgain.lower()
		if playAgain == 'y':
			_ = system('cls') #clear screen
			reset()
		else:
			quit()

	#Kör spelet om och om igen!
	play(b, k, startTime)


reset() # ta bort sen