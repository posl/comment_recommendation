def main():
    n = int(input())
    A = list(map(int, input().split()))
    s = sum(A)
    left = 0
    right = 0
    left_s = A[0]
    right_s = s - A[0]
    min_dif = abs(left_s - right_s)
    for i in range(n - 1):
        if left_s < right_s:
            left += 1
            left_s += A[left]
        else:
            right += 1
            right_s -= A[right]
        dif = abs(left_s - right_s)
        if dif < min_dif:
            min_dif = dif
    print(min_dif)

if __name__ == '__main__':
    main()