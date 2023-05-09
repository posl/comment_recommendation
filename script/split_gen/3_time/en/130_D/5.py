def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    count = 0
    i = 0
    j = 0
    while i < N:
        while j < N:
            sum += A[j]
            if sum >= K:
                count += N - j
                break
            j += 1
        sum -= A[i]
        i += 1
    print(count)
main()
