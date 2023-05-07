def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        total += A[i]
    ans = (T // total) * N
    T %= total
    for i in range(N):
        if T >= A[i]:
            ans += 1
            T -= A[i]
        else:
            break
    print(ans, T)

if __name__ == '__main__':
    main()