# sort vs sorted

print("Using sorted does not change the original list")
L = [1,3,2,4,7,1]
print(sorted(L))
print(L)

print("Now calling .sort() method")
print(L.sort())
print(L)
print("L has now changed")

