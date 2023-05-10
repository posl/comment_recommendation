def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    now = 0
    for i in range(61):
        if (K >> i) & 1:
            now = A[now]
        A = [A[A[j]] for j in range(N)]
    print(now + 1)
