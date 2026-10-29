numbers = [2, 3, 2, 5, 3, 2, 5, 8]
frequency = {}
for numbers in numbers:
    if numbers not in frequency:
        frequency[numbers]  =1
    else:
        frequency[numbers] +=1
print(frequency)
