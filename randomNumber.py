import random

randomNumber = random.randint(1, 100)
correct = False
counter = 0
while(correct == False):
    try:
        guessedNumber = int(input("Please guess a number: "))
    except ValueError:
        print("Please enter a valid integer!⚠️") 
        continue
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
