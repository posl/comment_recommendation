def main():
    import sys
    readline = sys.stdin.readline
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    cnt = 0
    for i in range(N):
        for j in range(i, N):
            if sum(A[i:j+1]) == K:
                cnt += 1
    print(cnt)
