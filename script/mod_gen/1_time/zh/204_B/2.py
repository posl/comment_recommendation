def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] > 10:
            count += A[i] - 10
    print(count)

if __name__ == '__main__':
    main()