def solve():
    N,X = map(int,input().split())
    S = input()
    res = X
    for i in range(N):
        if S[i] == "U":
            res = res // 2
        elif S[i] == "L":
            res = res * 2 - 1
        else:
            res = res * 2 + 1
    print(res)

if __name__ == '__main__':
    solve()