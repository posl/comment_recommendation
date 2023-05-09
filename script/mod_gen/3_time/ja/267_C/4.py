def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(max([sum(A[i:i+M]) * (i+1) for i in range(N-M+1)]))

if __name__ == '__main__':
    main()