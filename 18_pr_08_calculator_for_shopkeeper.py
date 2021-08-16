sum = 0
while (True):
    userInput = input("Enter the item price or press q to quit: \n")
    if (userInput!='q'):
        sum = sum + int(userInput)
        print(f"Order total so far:{sum}")
else:
    print(f"Your Bill toltal is {sum}. Thanks for shoping with us ")
    