def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    sum_A = sum(A)
    if sum_A > X:
        print(N + (X - 1) // sum_A * N)
    else:
        print(N + X // sum_A * N)

if __name__ == '__main__':
    main()