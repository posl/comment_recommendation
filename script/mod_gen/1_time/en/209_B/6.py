def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(1, N + 1):
        if i % 2 == 0:
            X -= A[i - 1] - 1
        else:
            X -= A[i - 1]
    if X >= 0:
        print('Yes')
    else:
        print('No')
main()

if __name__ == '__main__':
    main()