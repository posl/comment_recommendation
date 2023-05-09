def main():
    Q = int(input())
    A = []
    A2 = []
    for i in range(Q):
        c = list(map(int, input().split()))
        if c[0] == 1:
            A.append(c[1])
            A2.append(c[1])
        elif c[0] == 2:
            A = sorted(A, reverse=True)
            if len(A) < c[2]:
                print(-1)
            else:
                print(A[c[2]-1])
        elif c[0] == 3:
            A2 = sorted(A2)
            if len(A2) < c[2]:
                print(-1)
            else:
                print(A2[c[2]-1])
