def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if i == 0:
            print(A[i] - A[N-1], end=" ")
        else:
            print(A[i] - A[i-1], end=" ")

if __name__ == '__main__':
    main()