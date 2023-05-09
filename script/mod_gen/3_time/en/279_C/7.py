def solve():
    H,W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S = [sorted(S[i]) for i in range(H)]
    T = [sorted(T[i]) for i in range(H)]
    S.sort()
    T.sort()
    for i in range(H):
        if S[i] != T[i]:
            return "No"
    return "Yes"

if __name__ == '__main__':
    solve()