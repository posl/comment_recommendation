def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = A[::-1]
    for a in A:
        if N%a == 0:
            print(N - a)
            return

if __name__ == '__main__':
    main()