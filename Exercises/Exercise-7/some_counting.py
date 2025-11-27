# Exercise 7: Some Counting
# Demonstrates counting with for loops

def function(start, end, increment):
    for i in range(start, end, increment):
        print(i)

print("Counting from 0 to 50 in increments of 1")
function(0, 51, 1)

print("Counting from 50 to 0 in decrements of 1")
function(50, -1, -1)

print("Counting from 30 to 50 in increments of 1")
function(30, 51, 1)

print("Counting from 50 to 10 in decrements of 2")
function(50, 9, -2)

print("Counting from 100 to 200 in increments of 5")
function(100, 201, 5)