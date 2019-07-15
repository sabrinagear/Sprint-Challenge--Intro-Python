# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# name starts with 'D':
print("Starts with D:")
a = [x.name for x in humans if x.name.startswith("D")]
print(a)

# name ends in "e".
print("Ends with e:")
b = [x.name for x in humans if x.name.endswith("e")]
print(b)

# name starts with any letter between 'C' and 'G'
# inclusive.
print("Starts between C and G, inclusive:")
letters = map(chr, range(67, 72))
c = [y.name for x in letters for y in humans if y.name.startswith(x)]

print(c)

# all ages plus 10.
print("Ages plus 10:")
d = [x.age + 10 for x in humans]
print(d)

# name-age
print("Name hyphen age:")
e = [x.name + "-" + str(x.age) for x in humans]
print(e)

# ages of humans in range 27 to 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(x.name,x.age) for x in humans if x.age in range(27,33)]
print(f)

# all names uppercase
print("All names uppercase:")
g = [Human(x.name.upper(),x.age + 5) for x in humans]
print(g)

# square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(x.age) for x in humans]
print(h)
