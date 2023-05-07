def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    left = 0
    right = 0
    for i in range(N):
        left += A[i] / B[i]
        right += A[N - 1 - i] / B[N - 1 - i]
    if left == right:
        print(left)
    elif left > right:
        left = 0
        for i in range(N):
            left += A[i] / B[i]
            if left >= right:
                print(left)
                break
    else:
        right = 0
        for i in range(N):
            right += A[N - 1 - i] / B[N - 1 - i]
            if right >= left:
                print(right)
                break

if __name__ == '__main__':
    main()