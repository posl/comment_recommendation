def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 从左端开始燃烧
    left = 0
    for i in range(N):
        left += A[i] / B[i]
    # 从右端开始燃烧
    right = 0
    for i in range(N):
        right += A[N - i - 1] / B[N - i - 1]
    # 火焰相遇的位置
    meet = 0
    for i in range(N):
        meet += A[i] / B[i] * 0.5
    print(left - meet)
    print(right - meet)

if __name__ == '__main__':
    main()