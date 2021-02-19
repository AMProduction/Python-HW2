""" Task 3
Author: Andrii Malchyk
v.1.0
"""
print("Please, enter the number: ")
input_number = input()
sum = 0
if int(input_number) > 0:
    for number in input_number:
        if int(number) % 2 != 0:
            sum += int(number)
        else:
            continue
else:
    print("The invalid input number!")
    exit()
print("The sum: ", sum)
