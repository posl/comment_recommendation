def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    ans = [i for i in range(1, N+1)]
    for i in range(Q-1, -1, -1):
        ans[i], ans[i+1] = ans[i+1], ans[i]
        if ans[i+1] == X[i]:
            ans[i+1], ans[i+2] = ans[i+2], ans[i+1]
    print(' '.join(list(map(str, ans))))
