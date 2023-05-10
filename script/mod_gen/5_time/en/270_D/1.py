def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    while N > 0:
        N = N - A[i]
        i = i + 1
    print(i)
main()

if __name__ == '__main__':
    main()