def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    print(sum(A[:K]))

if __name__ == '__main__':
    main()