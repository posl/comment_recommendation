def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] = A[i] / 2
            count += 1
        while A[i] % 3 == 0:
            A[i] = A[i] / 3
            count += 1
    if len(set(A)) == 1:
        print(count)
    else:
        print(-1)

if __name__ == '__main__':
    main()