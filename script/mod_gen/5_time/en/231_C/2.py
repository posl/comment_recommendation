def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(Q):
        x = int(input())
        l = 0
        r = N-1
        while l < r:
            m = (l+r)//2
            if A[m] >= x:
                r = m
            else:
                l = m+1
        if A[l] >= x:
            print(N-l)
        else:
            print(0)
main()
