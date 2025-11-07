question = "What is the capital of France?"
answer = input(question + " ")
correctanswer = "paris";

if answer.lower() == correctanswer:
    print("Answer is correct!");
else:
    print("Answer is wrong!");

# if the answer is correct, print "Answer is correct!", otherwise print "Answer is wrong!"
# Example:
# Input: PaRiS (regardless of capital letters)
# Output: Answer is correct!
# Input: London
# Output: Answer is wrong!
