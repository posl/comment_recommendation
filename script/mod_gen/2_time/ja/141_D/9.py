def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(max(0, A[0] - (A[0] >> M)))

if __name__ == '__main__':
    main()