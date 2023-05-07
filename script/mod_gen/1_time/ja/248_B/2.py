def main():
    A, B, K = map(int, input().split())
    for i in range(K):
        if A % 2 == 0:
            A = A // 2
            B = B + A
        else:
            A = (A - 1) // 2
            B = B + (A + 1)
    print(A, B)

if __name__ == '__main__':
    main()