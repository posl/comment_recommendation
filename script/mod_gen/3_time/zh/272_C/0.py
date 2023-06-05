def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = -1
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] + A[j]) % 2 == 0:
                ans = max(ans, A[i] + A[j])
    print(ans)

if __name__ == '__main__':
    main()