def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [[i, A[i]] for i in range(2**N)]
    while len(A) > 2:
        B = []
        for i in range(0, len(A), 2):
            if A[i][1] > A[i+1][1]:
                B.append(A[i])
            else:
                B.append(A[i+1])
        A = B
    if A[0][1] > A[1][1]:
        print(A[1][0] + 1)
    else:
        print(A[0][0] + 1)
main()

if __name__ == '__main__':
    main()