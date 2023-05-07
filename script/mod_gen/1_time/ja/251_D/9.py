def main():
    W = int(input())
    N = W
    A = [1] * W
    for i in range(1, W):
        if N % 2 == 0:
            N = N // 2
            A[i] = 2
        else:
            N = N // 2 + 1
            A[i] = 2
    print(W)
    print(*A)
main()

if __name__ == '__main__':
    main()