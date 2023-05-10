def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] = A[i] % 200
    A.sort()
    ans = 0
    for i in range(N):
        j = i + 1
        while j < N and A[i] == A[j]:
            j += 1
        ans += (j - i) * (j - i - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()