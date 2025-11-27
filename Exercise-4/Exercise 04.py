# Exercise 4: Primitive Quiz (Advanced Requirements)
# This version accepts any capitalization and is prepared for multiple questions.

question = "What is the capital of France?"
answer = input(question + " ")
correctanswer = "paris"

# Accept the answer regardless of capitalization
if answer.lower() == correctanswer:
    print("Answer is correct!")
else:
    print("Answer is wrong!")

# This file demonstrates the advanced features:
# - Accepting multiple forms of capitalization
# - Structure suitable for expanding to multiple questions
