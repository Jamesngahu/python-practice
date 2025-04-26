number = input("Enter any number here:")
#prompts the user to give a number
added_digits = 0
#initialises the value to zero

for n in number:
    added_digits = added_digits + int(n)
#creates a loop that adds each digit in the number to the total value

print("The sum of digits in the number is",added_digits)
#prints the final number