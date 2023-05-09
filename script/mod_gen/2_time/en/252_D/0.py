def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            k = bisect.bisect_left(A, A[i]+A[j])
            ans += k-j-1
    print(ans)

if __name__ == '__main__':
    main()