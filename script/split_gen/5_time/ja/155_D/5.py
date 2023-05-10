def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    left = -10**18-1
    right = 10**18+1
    while left+1 < right:
        mid = (left+right)//2
        count = 0
        for i in range(N):
            if A[i] < 0:
                l = -1
                r = N
                while l+1 < r:
                    m = (l+r)//2
                    if A[i]*A[m] < mid:
                        r = m
                    else:
                        l = m
                count += N-r
            else:
                l = -1
                r = N
                while l+1 < r:
                    m = (l+r)//2
                    if A[i]*A[m] < mid:
                        l = m
                    else:
                        r = m
                count += r
            if A[i]*A[i] < mid:
                count -= 1
        count //= 2
        if count < K:
            left = mid
        else:
            right = mid
    print(left)
