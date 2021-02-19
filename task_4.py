""" Task 4
Author: Andrii Malchyk
v.1.0
"""
print("Please, enter the number: ")
input_number = input()
sum = 0
if int(input_number) > 0:
    bin_input_number = [int(i) for i in bin(int(input_number))[2:]]
    print("Binary: ", bin(int(input_number)))
    for num in bin_input_number:
        if num == 1:
            sum += 1
        else:
            continue
else:
    print("The invalid input number!")
    exit()
print("The sum: " + str(sum))
