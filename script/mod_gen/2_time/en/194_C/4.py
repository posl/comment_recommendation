def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    sum = 0
    for i in range(1,N):
        for j in range(i):
            sum += (A[i] - A[j]) ** 2
    print(sum)

if __name__ == '__main__':
    main()