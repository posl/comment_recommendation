def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(Q):
        x = int(input())
        l = 0
        r = N-1
        while r-l>1:
            m = (l+r)//2
            if A[m] >= x:
                r = m
            else:
                l = m
        if A[l] >= x:
            print(N-l)
        else:
            print(N-r)

if __name__ == '__main__':
    main()