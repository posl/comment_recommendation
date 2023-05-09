def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    N -= sum(A)
    if N < 0:
        N = -1
    print(N)

if __name__ == '__main__':
    main()