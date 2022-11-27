# Owen Kroeger
# My Own Work


A = {2, 4, 5}
B = {2, 4, 6, 8, 10}

print(f'Set A: {A}')
print(f'Set B: {B}')
print()

# union
print("A union B")
C = A.union(B)
print(C)

# intersection
print()
print("A intersection B")
C = A.intersection(B)
print(C)

# difference
print()
print("A difference B")
C = A.difference(B)
print(C)

# symmetric difference
print()
print("A symmetric difference B")
C = A.symmetric_difference(B)
print(C)
print()

# function that tests if A is a subset of B (takes two sets as parameters (A and B))
def isSubset(A, B):

    print(A)
    print(B)
    print()

    # join A and B together (will not include repeats)
    C = A.union(B)

    # if A and B joined and nothing changed, then all of A existed in B
    # therefore, A is a subset
    if(C == B):
        print("A is a subset of B.")
    else:
        print("A is not a subset of B.")

    print()

isSubset(A, B)