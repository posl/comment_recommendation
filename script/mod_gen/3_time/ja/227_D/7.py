def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    print(A[K-1])

if __name__ == '__main__':
    main()