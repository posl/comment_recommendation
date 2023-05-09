def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    x = [int(input()) for i in range(Q)]
    B = sorted(A)
    for i in range(Q):
        l = 0
        r = N
        while l < r:
            mid = (l+r)//2
            if B[mid] >= x[i]:
                r = mid
            else:
                l = mid+1
        print(N-l)

if __name__ == '__main__':
    main()