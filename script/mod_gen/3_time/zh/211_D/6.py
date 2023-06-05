def main():
    N, M = map(int, input().split())
    AB = [map(int, input().split()) for _ in range(M)]
    A, B = [list(i) for i in zip(*AB)]
    print(A, B)
    print(N, M)
    pass

if __name__ == '__main__':
    main()