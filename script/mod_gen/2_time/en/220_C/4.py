def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 100
    B_sum = [0]
    for i in range(len(B)):
        B_sum.append(B_sum[-1] + B[i])
    for i in range(1, 100):
        if B_sum[i] > X:
            break
    else:
        i = 1
    print((X - B_sum[i - 1]) // A[i - 1] + (i - 1) * N)

if __name__ == '__main__':
    main()