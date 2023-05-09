def main():
    N = int(input())
    A = [0] * (N + 1)
    for i in range(N - 1):
        a, b = map(int, input().split())
        A[a] += 1
        A[b] += 1
    print('Yes' if A.count(N - 1) == 1 and A.count(1) == N - 1 else 'No')

if __name__ == '__main__':
    main()