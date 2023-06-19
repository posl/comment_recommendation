def monster(A, B, C, D):
    while True:
        C = C - B
        if C <= 0:
            return "Yes"
        A = A - D
        if A <= 0:
            return "No"
A, B, C, D = map(int, input().split())
print(monster(A, B, C, D))
