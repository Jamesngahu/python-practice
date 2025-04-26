word = input("Enter a word:")
#prompts the user to give a word
reversed_word = ""
#created an empty string that will hold the reversed letters
#one by one until its a full word
for char in word:
    reversed_word = char + reversed_word
    #created a loop that adds the reversed letters until its a word

print("The reversed word is",reversed_word)
#gives the final word