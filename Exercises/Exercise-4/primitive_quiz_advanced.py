# Exercise 4: Primitive Quiz (Advanced)
# Handles capitalization and is prepared for multiple questions

question = "What is the capital of France?"
answer = input(question + " ")
correctanswer = "paris"

if answer.lower() == correctanswer:
    print("Answer is correct!")
else:
    print("Answer is wrong!")

# Can be expanded to multiple questions easily