def main():
    N, M = map(int, input().split())
    ans = [0] * M
    for _ in range(N):
        *A, = map(int, input().split())
        for a in A:
            ans[a-1] += 1
    print(ans.count(N))
