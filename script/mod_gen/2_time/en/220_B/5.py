def main():
    # K = int(input())
    # A, B = map(int, input().split())
    K = 7
    A, B = 123, 456
    A = str(A)
    B = str(B)
    A10 = 0
    B10 = 0
    for i in range(len(A)):
        A10 += int(A[len(A) - i - 1]) * (K ** i)
    for i in range(len(B)):
        B10 += int(B[len(B) - i - 1]) * (K ** i)
    print(A10 * B10)

if __name__ == '__main__':
    main()