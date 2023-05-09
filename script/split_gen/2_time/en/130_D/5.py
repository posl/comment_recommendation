def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    i = 0
    j = 0
    sum = 0
    while True:
        if sum < K:
            if j >= N:
                break
            sum += A[j]
            j += 1
        else:
            ans += N - j + 1
            sum -= A[i]
            i += 1
    print(ans)
