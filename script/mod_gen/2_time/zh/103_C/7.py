def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    f = 0
    for i in range(1, N):
        f += A[i] - A[i - 1]
    print(f)

if __name__ == '__main__':
    main()