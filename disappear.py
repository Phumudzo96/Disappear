sentence = input("Enter a sentence: ") # Ask the user to enter a sentence
remove = input("Which letters would you like to remove: ")

# Select all the letters you want to disapear
sentence1 = sentence
for letter in remove:
    sentence1 = sentence1.replace(letter,"")


print(sentence1) # result of the sentence without some words 

