""" Task 5
Author: Andrii Malchyk
v.1.0
"""


def fibonacci(number):
    if number <= 1:
        return (number)
    else:
        return (fibonacci(number-1) + fibonacci(number-2))


print("Please, enter the number: ")
input_number = input()
sum = 0

print("The Fibonacci Sequence:")
for i in range(int(input_number)):
    print(fibonacci(i))
    sum += fibonacci(i)
print("The sum of the Fibonacci Sequence: ", sum)
