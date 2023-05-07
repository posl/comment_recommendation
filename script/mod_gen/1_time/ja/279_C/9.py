def solve():
    H,W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    #S,Tを縦に並べたものを比較する
    for i in range(W):
        s = [s[i] for s in S]
        t = [t[i] for t in T]
        if sorted(s) != sorted(t):
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    solve()