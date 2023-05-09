def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    for x in X:
        print(sum(abs(a - x) for a in A))

if __name__ == '__main__':
    main()