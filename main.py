import random
attempt=0
level=input("enter your difficilty level\n for Easy press 1\n For Medium press 2\n For Hard press 3\n :")
if level=="1":
        number=random.randint(1,50)
elif level=="2":
            number=random.randint(1,100)
elif level=="3":
            number=random.randint(1,500)
while True:
    #numbers are picked according to level
    
    try:    
        user_guess=int(input("Guess a number: "))
        attempt=attempt+1
    except ValueError:
           print("Enter numbers only!!")
           continue
# guessed succcessfully shows atempts
    if(user_guess==number and level=="1"):
        print("Congrats you guessed right the number is ", number)
        break
    elif(user_guess==number and level=="2"):
        print("Congrats you guessed right the number in ",attempt,"attempt")
        break
    elif(user_guess==number and level=="3"):
        print("Congrats you guessed right the number in ",attempt,"attempt")
        break
    #if guess number is smaller it count attempts and terminates as it reached max attempt for the level
    elif(user_guess< number and level=="1"):
        print("Oops, your guess is smaller than the original number, Try a greater number")
    elif(user_guess< number and level=="2"):
        
        if attempt==10:
             print("Out of attempts")
             break
        print("Oops, your guess is smaller than the original number, Try a greater number")
        print("Attempt:",attempt)
        print("Attempts remaning: ",10-attempt)
    elif(user_guess< number and level=="3"):
        
        if attempt==5:
                     print("Out of attempts")
                     break
        print("Oops, your guess is smaller than the original number, Try a greater number")
        print("Attempt:",attempt)
        print("Attempts remaning: ",5-attempt)
        # if guessed number is greater , attempt counter, terminates when max attempt reached
    elif (user_guess> number and level=="1"):
        print("Opps, your guess is greater than original number, Try a Smaller Number")
    elif(user_guess> number and level=="2"):
            
            if attempt==10:
                         print("Out of attempts")
                         break
            print("Oops, your guess is greater than the original number, Try a smaller number")
            print("Attempt:",attempt)
            print("Attempts remaning: ",10-attempt)
    elif(user_guess> number and level=="3"):
                
                if attempt==5:
                             print("Out of attempts")
                             break
                print("Oops, your guess is greater than the original number, Try a smaller number")
                print("Attempt:",attempt)
                print("Attempts remaning: ",5-attempt)
     
    