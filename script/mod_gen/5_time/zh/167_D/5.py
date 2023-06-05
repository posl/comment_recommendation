def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    for j in range(K):
        i = A[i] - 1
    print(i + 1)

if __name__ == '__main__':
    main()