print( "Welcome to Hangaman! You will have 10 guesses of letters to try and guess the six letter word word. If you get a letter correct, you get your guess back!" )
word="carrot"
score = 10
while score != 0 or user==word:
    print("Enter your guess!")
    user = input()
    if user == word:
        score += 1
        print("Correct! You get a life back.")
        print("Your new score is now ", score)

    elif user != word:
        score -= 1
        print("Incorrect! You lost a life.")
        print("Your new score is now ", score)
        if score == 0:
            print("You lose!")



print("If you want to play again, type yes, if you are done for now, type no.")
answer=input()
answer=answer.split(" ")
sanswer=[x.lower()for x in answer]
yes=["yes"]
no=["no"]
if sanswer == no:
        print("Thanks for playing my game!")
elif sanswer == yes:
    print("OK! Try and beat your high score!")
else:
    print("Please enter a correct input.")

    def scoreboard (score):
        total=score+1
        return total
    score=10
    y=scoreboard(score)
    print(y)