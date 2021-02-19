""" Task 2
Author: Andrii Malchyk
v.1.0
"""
print("Please, enter the number 100<=n<=999: ")
input_number = input()
if 100 <= int(input_number) <= 999:
    output_number = [int(x) for x in str(input_number)]
    output_number.sort(reverse=True)
else:
    print("The input number is out of range!")
    exit()
for x in output_number:
    print(x, end="")
