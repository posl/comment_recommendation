def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    i = 0
    j = 0
    s = 0
    while i < N:
        while j < N and s < K:
            s += A[j]
            j += 1
        if s < K:
            break
        ans += N - j + 1
        s -= A[i]
        i += 1
    print(ans)
