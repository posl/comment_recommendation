def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(n):
        sum += A[i] * (n - 1 - i) - A[i] * i
    print(sum)

if __name__ == '__main__':
    main()