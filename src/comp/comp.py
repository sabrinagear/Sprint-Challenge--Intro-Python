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
a = []
for x in humans:
    if x.name.startswith("D"):
        a.append(x.name)
print(a)

# name ends in "e".
print("Ends with e:")
b = []
for x in humans:
    if x.name.endswith("e"):
        b.append(x.name)
print(b)

# name starts with any letter between 'C' and 'G'
# inclusive.
print("Starts between C and G, inclusive:")
c = []
tr = map(chr, range(67, 72))
c = []
for x in tr:
    for y in humans:
        if y.name.startswith(x):
            c.append(y.name)
print(c)

# all ages plus 10.
print("Ages plus 10:")
d = []
for x in humans:
    d.append(x.age + 10)
print(d)

# name-age
print("Name hyphen age:")
e = []
for x in humans:
    e.append(x.name + "-" + str(x.age))
print(e)

# ages of humans in range 27 to 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for x in humans:
    if x.age in range(27,33):
        f.append((x.name,x.age)) 
print(f)

# all names uppercase
print("All names uppercase:")
g = []
for x in humans:
    g.append(Human(x.name.upper(),x.age + 5))
print(g)

# square root of all the ages.
print("Square root of ages:")
import math
h = []
for x in humans:
    h.append(math.sqrt(x.age))
print(h)
