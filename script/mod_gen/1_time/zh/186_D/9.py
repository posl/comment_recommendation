def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N):
        sum += A[i] * i - A[i] * (N - 1 - i)
    print(sum)

if __name__ == '__main__':
    main()