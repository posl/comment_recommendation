def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    sum = 0
    for i in range(1, N):
        sum += A[i] - A[i-1]
    print(sum * 2)

if __name__ == '__main__':
    main()