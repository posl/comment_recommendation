def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    count = 0
    for i in range(N):
        while A[i] % 2 == 0:
            count += 1
            A[i] /= 2
    print(count)

if __name__ == '__main__':
    main()