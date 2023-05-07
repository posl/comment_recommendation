def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1]*N
    for i in range(N):
        P[i] -= 1
    for i in range(N):
        if ans[i] != -1:
            continue
        cnt = 1
        j = i
        while ans[j] == -1:
            ans[j] = cnt
            cnt += 1
            j = P[j]
    for i in range(N):
        if ans[i] <= K:
            print(i+1)
