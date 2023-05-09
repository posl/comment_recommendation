def main():
    A, B, C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            return
    print(-1)
