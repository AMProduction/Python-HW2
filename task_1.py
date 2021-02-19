""" Task 1
Author: Andrii Malchyk
v.1.0
"""
print("Please, enter the number: ")
input_number = int(input())
if input_number > 0:
    output_number = input_number ** 2
elif input_number < 0:
    output_number = abs(input_number)
else:
    output_number = 0
print(output_number)
