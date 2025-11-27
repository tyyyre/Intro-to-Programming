# Exercise 4: Primitive Quiz (Basic)
# Ask the user "What is the capital of France?" and check the answer

question = "What is the capital of France?"
answer = input(question + " ")
correctanswer = "paris"

if answer.lower() == correctanswer:
    print("Answer is correct!")
else:
    print("Answer is wrong!")