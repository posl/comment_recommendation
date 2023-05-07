def main():
    N, M = map(int, input().split())
    road = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        road[A-1].append(B-1)
        road[B-1].append(A-1)
    ans = [0 for i in range(N)]
    ans[0] = 1
    for i in range(N):
        for j in road[i]:
            ans[j] += ans[i]
            ans[j] %= 10**9 + 7
    print(ans[N-1])
