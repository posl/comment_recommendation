def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    for i in range(N):
        B.append(A[i][0] + A[i][1] - 1)
    B.sort()
    for i in range(N):
        if i == 0:
            print(B[i], end = " ")
        else:
            print(B[i] - B[i-1], end = " ")
    print()

if __name__ == '__main__':
    main()