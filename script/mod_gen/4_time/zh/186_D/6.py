def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N):
        sum += A[i] * i - A[i] * (N - i - 1)
    print(sum)

if __name__ == '__main__':
    main()