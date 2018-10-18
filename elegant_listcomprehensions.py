#elements with single letter shorthands

# the approach without list comprehensions
elements = 'ISPOCHNBFWVKUY'
elements2 = []
for element in elements:
    elements2.append((element))

print(elements2)

# using list comprehensions
elements_with_single_letter_shorthands = [element for element in elements]
print(elements2)
