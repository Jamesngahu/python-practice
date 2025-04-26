num = int(input("Enter any number:"))
#prompts the user to enter a number
x = 1
#sets the initial value of a variable x to 1
while num > 0:
    """"creates a loop that executes the function
    as long as the value of num is more than 0"""
    x *= num
    #multiplies x by the value of num and stores it as its new value
    num = num -1
    # subtracts num by 1 after each step

print("The factorial is:",x)
#gives the factorial as the final value of x