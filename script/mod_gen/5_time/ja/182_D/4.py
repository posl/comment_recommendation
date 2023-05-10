def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    max = 0
    for i in range(N):
        sum += A[i]
        if max < sum:
            max = sum
    print(max)

if __name__ == '__main__':
    main()