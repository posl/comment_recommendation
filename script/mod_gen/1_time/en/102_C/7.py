def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += A[i] - (i+1)
    sum = abs(sum)
    print(sum)

if __name__ == '__main__':
    main()