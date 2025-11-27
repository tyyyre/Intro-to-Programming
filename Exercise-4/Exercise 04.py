# Exercise 4: Primitive Quiz (Basic Requirements)
# This program asks the user "What is the capital of France?" and checks the answer.

question = "What is the capital of France?"
answer = input(question + " ")
correctanswer = "paris"

# Check the answer (case-insensitive)
if answer.lower() == correctanswer:
    print("Answer is correct!")
else:
    print("Answer is wrong!")
