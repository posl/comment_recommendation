def main():
    N = int(input())
    A = list(map(int, input().split()))
    max = 0
    sum = 0
    for i in range(N):
        if sum < 0:
            sum = 0
        sum += A[i]
        if max < sum:
            max = sum
    print(max)

if __name__ == '__main__':
    main()