def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #init
    t = 0
    l = 0
    r = 0
    for i in range(N):
        t += A[i]/B[i]
        l += A[i]
        r += A[i]/B[i]
    #binary search
    while r-l > 10**(-6):
        m = (l+r)/2
        if m < t/2:
            l = m
        else:
            r = m
    #calc
    ans = 0
    for i in range(N):
        if r > A[i]/B[i]:
            ans += A[i]/B[i]**2
            r -= A[i]/B[i]
        else:
            ans += r**2/B[i]
            break
    print(ans)

if __name__ == '__main__':
    main()