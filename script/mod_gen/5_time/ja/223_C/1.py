def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    left = 0
    right = 10**18
    while right - left > 10**(-6):
        mid = (left + right) / 2
        t = 0
        for i in range(N):
            t += (mid - A[i]) / B[i]
        if t < mid:
            left = mid
        else:
            right = mid
    print(left)

if __name__ == '__main__':
    main()