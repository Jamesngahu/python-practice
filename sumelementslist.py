def sum(score):
    sum = 0
    for n in score:
        sum = sum + n
    return sum
my_scores=[51, 11, 10, 5]
result = sum(my_scores)
print(f"The total score is: {result}")