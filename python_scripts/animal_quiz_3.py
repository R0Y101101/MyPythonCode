#python 3

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:   
        if guess.lower() == answer.lower():
            print('correct answer')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry wrong answer. Try again. ')
            attempt = attempt + 1
            
        if attempt == 3:
            print('The correct answer is ' + answer)
        
                                
score = 0

name = input('What is your name?')
greeting = 'Hello ' + name
print(greeting)


print('Guess the Animal!')
guess1 = input('Which bear lives at the North Pole? ')
check_guess(guess1, 'polar bear')
guess2 = input('Which is the fastest land animal? ')
check_guess(guess2, 'cheetah')
guess3 = input('which is the largest animal? ')
check_guess(guess3, 'blue whale')
print ('BONUS!')
guess4 = input('Which planet is closest to the sun? ')
check_guess(guess4, 'mercury')
print('round 2!')
guess5 = input('who made the tesla car? ')
check_guess(guess5, 'elon musk')
guess6 = input('about how many languages are in the world?')
check_guess(guess6, '6,500')
print('SECOND BONUS')
guess7 = input('which of  these are a moon of jupiter, enceladus or io? ')
check_guess(guess7, 'io') 
guess8 = input('which galaxy is further from earth? \
A) Andromeda  B) Large Magellanic cloud  C) Gemineca  D) Wenmak? ')

check_guess(guess8, 'A')
guess9 = input
print('Play Again')

print('your score is ' + str(score))






