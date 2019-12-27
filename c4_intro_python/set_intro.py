a = [1,1,1,1,2,2,2,3,4,4,4,3,3,4,5]


print("a is a list with duplicate values:")
print(a)

print()
print("we can use the set() to convert the list into a set type: this is known as type casting")
print(set(a))

set_a = set(a)
set_a.add(1)
set_a.add(6)
print("adding values using .add() operation: only new unique values are added")
print(set_a)

print("use the & sign to show only the values in both sets")
print("other operation methods include .intersection(), .union(), .issuperset(), .issubset()")
