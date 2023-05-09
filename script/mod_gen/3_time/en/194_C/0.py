def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(1, N):
        for j in range(i):
            sum += (A[i] - A[j]) ** 2
    print(sum)

if __name__ == '__main__':
    main()