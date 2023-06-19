def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = []
    C = []
    for i in range(N):
        if A[i]%200 == 0:
            B.append(i+1)
        elif A[i]%200 == 100:
            C.append(i+1)
    if len(B) == 0 and len(C) == 0:
        print("No")
    elif len(B) == 0 and len(C) != 0:
        print("Yes")
        print("1",C[0])
        print("1",C[1])
    elif len(B) != 0 and len(C) == 0:
        print("Yes")
        print("1",B[0])
        print("1",B[1])
    else:
        print("Yes")
        print("1",B[0])
        print("1",C[0])
solve()
