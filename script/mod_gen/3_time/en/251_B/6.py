def solve(N, W, A):
    A.sort()
    A = A[::-1]
    a = A[0]
    b = A[1]
    c = A[2]
    d = A[3]
    e = A[4]
    f = A[5]
    g = A[6]
    ans = 0
    for i in range(W//a+1):
        for j in range((W-i*a)//b+1):
            for k in range((W-i*a-j*b)//c+1):
                for l in range((W-i*a-j*b-k*c)//d+1):
                    for m in range((W-i*a-j*b-k*c-l*d)//e+1):
                        for n in range((W-i*a-j*b-k*c-l*d-m*e)//f+1):
                            for o in range((W-i*a-j*b-k*c-l*d-m*e-n*f)//g+1):
                                if i*a+j*b+k*c+l*d+m*e+n*f+o*g <= W:
                                    ans += 1
    return ans
N, W = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, W, A))
