import random

randomNumber = random.randint(1, 100)
correct = False
counter = 0
while(correct == False):
    guessedNumber = int(input("Please guess a number: "))
    counter += 1
    if(randomNumber < guessedNumber):
        print("خیلی زیاد است!")
        continue
    elif(randomNumber > guessedNumber):
        print("خیلی کم است!")
        continue
    else:
        print("تبریک! درست حدس زدی!")
        correct = True

print(f"You guessed it in {counter} attempts!")
