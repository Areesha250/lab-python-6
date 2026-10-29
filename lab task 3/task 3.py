data = {'a':1, 'b':2, 'c':3}
new_data = {}
for key,value in data.items():
    new_data[value] = key
print(new_data)
