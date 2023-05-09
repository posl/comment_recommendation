def main():
    N, K, A = map(int, input().split())
    if N >= K:
        if A <= K:
            print(A)
        else:
            print(A % K)
    else:
        if A <= K:
            print(A % N)
        else:
            print((A % K) % N)

if __name__ == '__main__':
    main()