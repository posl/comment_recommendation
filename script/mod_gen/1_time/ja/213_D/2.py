def main():
    N = int(input())
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        A[i], B[i] = map(int, input().split())
    print(1, end = " ")
    for i in range(N-1):
        if A[i] == 1:
            print(B[i], end = " ")
            print(1, end = " ")
        elif B[i] == 1:
            print(A[i], end = " ")
            print(1, end = " ")
    print()

if __name__ == '__main__':
    main()