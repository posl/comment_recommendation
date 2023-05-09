def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(max(N-sum(A), -1))

if __name__ == '__main__':
    main()