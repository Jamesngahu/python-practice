#created a function total
def total(score):
    #initialised the local variable value to zero
    total = 0
    for n in score:
        total = total + n
        #created a loop that stores the value as it goes through items in the list in n
    return total
my_scores=[51, 11, 10, 5]
#created a scores list
result = total(my_scores)
#created a variable  result that calls the total function
print(f"The total score is: {result}")
#included an f-string to call the variable result