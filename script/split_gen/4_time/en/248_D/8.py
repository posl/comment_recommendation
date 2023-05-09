def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    cnt = [0]*(N+1)
    for i in range(N):
        cnt[A[i]] += 1
    for i in range(Q):
        L,R,X = queries[i]
        print(cnt[X])
