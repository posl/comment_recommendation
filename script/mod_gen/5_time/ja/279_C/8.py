def solve():
    H,W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    #print(H,W,S,T)
    S1 = ["".join(sorted(s)) for s in S]
    T1 = ["".join(sorted(t)) for t in T]
    #print(S1)
    #print(T1)
    if S1 == T1:
        print("Yes")
    else:
        print("No")
    return 0

if __name__ == '__main__':
    solve()