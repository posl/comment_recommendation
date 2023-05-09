def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * (10 ** 100)
    sum = 0
    for i in range(1, N * (10 ** 100) + 1):
        sum += B[i - 1]
        if sum > X:
            print(i)
            break

if __name__ == '__main__':
    main()