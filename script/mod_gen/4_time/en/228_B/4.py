def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A[X-1] = 0
    print(len(set(A)))

if __name__ == '__main__':
    main()