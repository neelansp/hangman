import  requests 
from bs4 import BeautifulSoup

r = requests.get("https://www.merriam-webster.com/word-of-the-day")
soup = BeautifulSoup(r.content, "html.parser")
wotd = soup.find("h1",attrs={"":""}).text
wotd = wotd.strip()

#r2 = requests.get("https://www.merriam-webster.com/word-of-the-day")
#soup = BeautifulSoup(r2.content, "html.parser")
wotde = soup.find("div",attrs={"class":"wotd-examples"}).text
wotde = wotde.strip()

def hiddenwotde(wotde, word):
    hiddenwotde = wotde.replace(word,"[ ? ]")
    print(hiddenwotde)



def wordblank(word,corguess,correct):
    for characters in word:
        if characters in corguess:
            print(characters, end = " ")
        elif characters == " ":
            print(" ", end = " ")
        else:
            print('_', end = " ")
            
def scaff(incorrect,top,bottom,dif):
    if incorrect == 0:
        print(top)
        print("  |    \n  |    \n  |    \n  |   ")
        print(bottom)
    elif incorrect == 1:
        print(top)
        print("  |    o\n  |    \n  |    \n  |   ")
        print(bottom)
    elif incorrect == 2:
        print(top)
        print("  |    o\n  |    |\n  |    \n  |   ")
        print(bottom)
    elif incorrect == 3:
        print(top)
        print("  |    o\n  |   /|\n  |    \n  |   ")
        print(bottom)
    elif incorrect == 4:
        print(top)
        print("  |    o\n  |   /|\\\n  |    \n  |   ")
        print(bottom)
    elif incorrect == 5:
        print(top)
        print("  |    o\n  |   /|\\\n  |    |\n  |   ")
        print(bottom)
    elif incorrect == 6:
        print(top)
        print("  |    o\n  |   /|\\\n  |    |\n  |   / ")
        print(bottom)
    else:
        print(top)
        print("  |    o\n  |   /|\\\n  |    |\n  |   / \\")
        print(bottom)
        print("You lose\nThe word was",word)
        if dif == "w":
            wotdeinput = input('Would you like the Word of the Day used in sentences?(type "yes or no") ')
            if wotdeinput == "yes":
                print(wotde)
        else:
            print("Thank you for playing!")
            
            
def easyhint(word, wordlist):
    if word == wordlist[0]:
        print('\nA type of plane')
    elif word == wordlist[1]:
        print('\nA type of chicken')
    elif word == wordlist[2]:
        print('\nSomething that bounces')
    elif word == wordlist[3]:
        print('\nIf you come in first place, you are number ___')
    elif word == wordlist[-3]:
        print('\nThe color of the sky')
    elif word == wordlist[-2]:
        print('\nIf you are not inside, you are ___side')
    else:
        print('\nA special treat that you eat on your Birthday')
        
letters = 'abcdefghijklmnopqrstuvwxyz '
bank = list(letters)
        
import random

#welcome prompt
print("Welcome to Hangman!")
while True:
    abinput = input("If you already know how to play type \"a\"\nIf you want to know how to play, type \"b\"\n")
    if abinput.lower() == 'b':
        print("Enter only one letter to try and guess the secret word. There are to modes, Partner mode and CPU mode. In Partner mode, you or your partner types in a word and you/your partner enters letters to guess the word. For CPU mode, the computer generates the word based on the difficulty you choose. You would then proceed to guess the word letter by letter. If you need help, you can type help for only the CPU mode.")
        pass
    elif abinput.lower() == 'a':
        pass
    else:
        print("\nPlease type \"a\" or \"b\"")
        
#game mode
    cpuor2play= input("If you are playing with a partner, type \"a\"\nIf you are playing against a cpu, type \"b\"\n")
    if cpuor2play.lower() == 'b':
        print('\nCPU mode has been chosen\n\n')
        dif = input('Choose your difficulty, "Easy", "Normal","Hard" or "the word of the day (w)" ').lower()
        while dif not in ['easy','normal','hard','w']:
            dif = input('Please only type "Easy", "Normal","Hard" or "the word of the day (w)": ')
        if dif == 'easy':
            print('If you type help, you also get hints for this mode!')
            wordlist = ['jet','hen','ball','one','blue','out','cake']
            word = random.choice(wordlist)
            break
        elif dif == 'normal':
            wordlist = ['sword','billy','hangman','python','neelan','coding','computer']
            word = random.choice(wordlist)
            break
        elif dif == 'hard':
            print('The limbs get drawn faster in hard mode! Be cautious with picking your letters!')
            wordlist = ['pterodactyl','minuscule','plagiarism','omnious','supercalifragilisticexpialidocious']
            word = random.choice(wordlist)
            break
        else:
            word = wotd
            break
    elif cpuor2play.lower() == 'a':
        dif = " "
        print("\npartner mode has been chosen\n")
        while True:
            word = input('Player 1: Enter a word that you want Player 2 to guess\nMAKE SURE YOU SCROLL TO THE BOTTOM TO HIDE WORD\n').lower()
            if word in bank:
                print("Enter a word that consists of only letters")
            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDONT SCROLL UP\nCurrently nothing is hanging!")
                break
        break
    else:
        print("\nPlease enter \"a\" or \"b\" to choose the mode")
top = " _______\n  |    |"     
bottom = " _|_\n|   |______\n|          |\n|__________|"
incorrect = 0 
correct = 0
scaff(incorrect,top,bottom,dif)
corguess = []
wordblank(word,corguess,correct)
letters = 'abcdefghijklmnopqrstuvwxyz '
bank = list(letters)
blankcount = 1
blankcounter = word.count(" ")
blankcount+=blankcounter
#guesses
while incorrect != 7:
    guess= input('\nGuess a letter\t').lower()
    if guess == 'quit':
        print("Thank you for playing!")
        break
    elif guess == 'help':
        scaff(incorrect,top,bottom,dif)
        wordblank(word,corguess,correct)
        print('\nThe letters you still can use are:', ' '.join(bank))
        if dif == 'easy':
            easyhint(word, wordlist)
    elif dif == "w" and guess  == "example":
        hiddenwotde(wotde,word)
    elif len(guess) != 1:
        print('please type only 1 letter')
    elif guess.isalpha() == False:
        print('please type a LETTER')
    elif guess not in bank:
        print("You already use this letter\nhere are the letters you can use:",' '.join(bank))
    else:
        bank.remove(guess)
        corguess.append(guess)
        if guess in word:
            print("correct")
            countletter = word.count(guess)
            if correct == len(word)-blankcount:
                print('YAY you win\nThe word was',word)
                if dif == "w":
                    wotdeinput = input('Would you like the Word of the Day used in sentences?(type "yes or no") ')
                    if wotdeinput == "yes":
                        print(wotde)
                        break
                    else:
                        print("Thank you for playing!")
                        break
                else:
                    break
            else:
                correct += countletter
            wordblank(word,corguess,correct)
        else:
            print("incorrect\nA limb has been added")
            if dif == 'hard':
                if incorrect == 0:
                    incorrect +=1
                elif incorrect ==1:
                    incorrect +=3
                elif incorrect == 4:
                    incorrect +=1
                else:
                    incorrect +=2
            else:
                incorrect +=1
            scaff(incorrect,top,bottom,dif)
            wordblank(word,corguess,correct)
