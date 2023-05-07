def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [i-1 for i in P]
    ans = [-1]*N
    card = [-1]*N
    for i in range(N):
        card[P[i]] = i
    for i in range(N):
        if ans[i] != -1:
            continue
        ans[i] = i+1
        j = i
        while card[j] >= K-1:
            ans[j] = i+1
            j = card[j] - K + 1
    for i in range(N):
        print(ans[i])
