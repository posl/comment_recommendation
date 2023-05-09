def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(sum(A[:A.index(N)]))

if __name__ == '__main__':
    main()