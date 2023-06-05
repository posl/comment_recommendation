def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    print(N, A, Q, BC)

if __name__ == '__main__':
    main()