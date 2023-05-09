def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if i == 0:
            print(A[1] + A[N-1], end=' ')
        elif i == N-1:
            print(A[N-2] + A[0], end=' ')
        else:
            print(A[i-1] + A[i+1], end=' ')

if __name__ == '__main__':
    main()