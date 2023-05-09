def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    minus = 0
    for i in range(N-1):
        if A[i]+minus < 0:
            if A[i]+A[i+1]+minus < 0:
                ans += abs(A[i]+A[i+1]+minus)
                minus = -1
            else:
                ans += abs(A[i]+minus)
                minus = A[i+1]
        else:
            minus += A[i+1]
    ans += abs(A[N-1]+minus)
    print(ans)

if __name__ == '__main__':
    main()