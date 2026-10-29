words = ['apple','ant', 'banana', 'ball', 'cat']
result = {}
for word in words:
    first_letter =word[0]
    if first_letter in result :

      result[first_letter].append(word)
    else:
        result[first_letter] = [word]
print(result)
