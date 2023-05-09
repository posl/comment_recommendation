def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for _ in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    for i in range(N):
        if i + 1 not in A and i + 1 not in B and i + 1 not in C and i + 1 not in D:
            print("Yes")
            return
    print("No")
