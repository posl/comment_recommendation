def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += i - bisect.bisect_left(A,A[i])
    print(ans)

if __name__ == '__main__':
    main()