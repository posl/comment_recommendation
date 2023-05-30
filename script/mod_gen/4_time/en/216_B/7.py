def solve():
    N = int(input())
    for i in range(N):
        S, T = input().split()
        for j in range(i):
            if S == Ss[j] and T == Ts[j]:
                print("Yes")
                return
        Ss.append(S)
        Ts.append(T)
    print("No")
Ss = []
Ts = []
solve()
