def main():
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    As.sort(reverse=True)
    for A in As:
        N -= A
        if N < 0:
            print(-1)
            return
    print(N)

if __name__ == '__main__':
    main()