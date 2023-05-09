def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    i = 1
    j = 1
    while i <= K:
        i += 1
        j = A[j]
        if j == 1:
            break
    if i <= K:
        K = (K - i) % (i - 1)
        for _ in range(K):
            j = A[j]
    print(j)

if __name__ == '__main__':
    main()