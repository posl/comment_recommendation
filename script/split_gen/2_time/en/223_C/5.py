def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    left = 0
    right = 100000
    while right - left > 0.0000000001:
        mid = (left + right) / 2
        #print("left: %f, right: %f, mid: %f" % (left, right, mid))
        t = 0
        for i in range(N):
            t = t + A[i] / (B[i] + mid)
        #print("t: %f" % t)
        if t < mid:
            right = mid
        else:
            left = mid
    print(mid)
