def main():
    N, M = map(int, input().split())
    k = [int(input()) for _ in range(M)]
    a = [list(map(int, input().split())) for _ in range(M)]
    print(N, M, k, a)
    pass

if __name__ == '__main__':
    main()