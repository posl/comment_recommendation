def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    for i in range(M):
        if (A[i] in C and B[i] in D) or (A[i] in D and B[i] in C):
            continue
        else:
            print("No")
            exit()
    print("Yes")
main()
