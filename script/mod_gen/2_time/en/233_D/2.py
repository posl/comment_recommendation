def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(N):
        A[i + 1] += A[i]
    counter = {}
    for a in A:
        if a in counter:
            counter[a] += 1
        else:
            counter[a] = 1
    ans = 0
    for a in A:
        if a + K in counter:
            ans += counter[a + K]
    print(ans)

if __name__ == '__main__':
    main()