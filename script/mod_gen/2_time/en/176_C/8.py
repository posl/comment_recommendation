def main():
    N = int(input())
    A = list(map(int, input().split()))
    height = 0
    for i in range(N):
        if A[i] > A[i-1]:
            height += A[i] - A[i-1]
    print(height)

if __name__ == '__main__':
    main()