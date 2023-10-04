print("Welcome to Mortgage Calulcator!")
try:
    salary = int(input("What is your salary? "))
except:
    print("Enter an integer number!")
    salary = int(input("What is your salary? "))
else:
    rate = 0
    if salary >= 2000:
        print("You are eligible for mortgage!")
        credit_score = int(input("What is your credit score? "))
        if credit_score > 800:
            rate = 4
            print("Interest rate: 4%")
        elif credit_score > 750:
            rate = 6
            print("Interest rate: 6%")
        else:
            rate = 8
            print("Interest rate: 8%")
        disability = input("Do you have any disability? Y or N.")
        if disability == "Y":
            rate -= 2
        print(f"Final interest rate: {rate}%")  
        

    else:
        print("Sorry, you are not eligible!")

finally:
    print("Thanks for using our calculator!")