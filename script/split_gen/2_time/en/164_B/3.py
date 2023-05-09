def main():
    A, B, C, D = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)
    
    while True:
        C = C - B
        if C <= 0:
            print("Yes")
            break
        A = A - D
        if A <= 0:
            print("No")
            break
