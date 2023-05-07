def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 二分探索
    left = 0
    right = 10**9 + 1
    while right - left > 10**(-5):
        mid = (right + left) / 2
        t = 0
        for i in range(N):
            t += (A[i] / mid) * B[i]
        if t >= 2:
            left = mid
        else:
            right = mid
    print(left)

if __name__ == '__main__':
    main()