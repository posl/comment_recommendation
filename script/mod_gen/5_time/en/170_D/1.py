def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
        elif A[i] % A[i-1] != 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()