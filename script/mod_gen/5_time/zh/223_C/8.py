def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    left = 0
    right = sum(A)
    while right - left > 10**(-6):
        mid = (right + left) / 2
        t = 0
        for i in range(N):
            t += A[i] / (B[i] + mid)
        if t > mid:
            left = mid
        else:
            right = mid
    print(left)

if __name__ == '__main__':
    main()