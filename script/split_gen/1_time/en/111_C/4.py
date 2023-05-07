def solve():
    N = int(input())
    V = list(map(int, input().split()))
    V1 = V[::2]
    V2 = V[1::2]
    V1.sort()
    V2.sort()
    if V1[0] == V1[-1]:
        if V2[0] == V2[-1]:
            print(0)
        else:
            print(N//2 - V2.count(V2[0]))
    elif V2[0] == V2[-1]:
        print(N//2 - V1.count(V1[0]))
    else:
        print(N//2 - V1.count(V1[0]) + N//2 - V2.count(V2[0]))
