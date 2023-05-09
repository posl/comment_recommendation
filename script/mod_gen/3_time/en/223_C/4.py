def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    left = 0
    right = 0
    for i in range(N):
        left += A[i] / B[i]
    for i in range(N):
        right += A[i] / B[i]
    right /= 2
    while True:
        tmp = 0
        for i in range(N):
            tmp += A[i] / B[i]
        if left < right:
            left = right
            right = (left + tmp) / 2
        else:
            right = left
            left = (right + tmp) / 2
        if abs(left - right) < 0.000000000000001:
            break
    print(left)

if __name__ == '__main__':
    main()