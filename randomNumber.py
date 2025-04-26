import random

while(True):
    random_number = random.randint(1, 100)
    correct = False
    attempt = 5
    counter = 0
    while(attempt > 0):
        try:
            guessed_number = int(input("Please guess a number: "))
        except ValueError:
            print("Please enter a valid integer!⚠️") 
            continue
        
        attempt -= 1
        counter += 1
        if(random_number < guessed_number):
            print("خیلی زیاد است!")
            continue
        elif(random_number > guessed_number):
            print("خیلی کم است!")
            continue
        else:
            print("تبریک! درست حدس زدی!")
            correct = True
            break
    if(correct == False):
        print("Sorry, you have run out of attempts.")
        print(f"The correct number was {random_number}.")

    print(f"You guessed it in {counter} attempts!")


    play_again = input("Do you want to play again?[y/n]").lower()
    if(play_again != "y"):
        print("Thanks for playing! Goodbye!")
        break