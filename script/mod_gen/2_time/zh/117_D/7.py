def main():
    N, K = map(int, input().split())
    A = map(int, input().split())
    A = list(A)
    A.sort()
    ans = 0
    for i in range(40, -1, -1):
        count = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                count += 1
        if count <= N//2:
            if ans + (1 << i) <= K:
                ans += (1 << i)
    sum = 0
    for i in range(N):
        sum += ans ^ A[i]
    print(sum)

if __name__ == '__main__':
    main()