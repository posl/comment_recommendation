def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] + sorted([A[i] - A[i - 1] for i in range(1, N)])
    print(sum(B[-M:]))

if __name__ == '__main__':
    main()