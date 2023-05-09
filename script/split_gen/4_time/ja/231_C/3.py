def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(Q):
        x = int(input())
        if x < A[0]:
            print(N)
        elif x >= A[-1]:
            print(0)
        else:
            l = 0
            r = N-1
            while l+1 < r:
                m = (l+r)//2
                if A[m] >= x:
                    r = m
                else:
                    l = m
            print(N-r)
