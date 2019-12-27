A = [1,2,3,4]
print("A is a list")
print(id(A))

print()
print("Regular assignment to a new var:  B = A")
B = A
print(id(B))

print()
print("Assignment with [:] operator on A:  C = A[:]")
C = A[:]
print(id(C))

