num = int(input("Enter any number:"))
#prompts user to enter a number

def factorial(m):
    #creates a function factorial with one argument m

  if m == 0 or m==1:
    return 1
  #this is the base case which checks if the number is zero or one
  #and stops the recursion there by giving 1

  else:
      return m * factorial(m -1)
#if the value isn't one it calls the function and multiplies it with m -1 until it reaches base case

x = factorial(num)
#calls the function with the user's input and stores the value in the variable x
print("The factorial is:",x)