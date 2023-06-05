def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    max = 0
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += A[j] % A[i]
        if sum > max:
            max = sum
    print(max)

if __name__ == '__main__':
    main()