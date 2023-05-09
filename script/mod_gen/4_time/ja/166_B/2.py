def main():
    N, K = map(int, input().split())
    A = [0] * K
    for i in range(K):
        d = int(input())
        A[i] = list(map(int, input().split()))
    A = sum(A, [])
    print(N - len(set(A)))

if __name__ == '__main__':
    main()