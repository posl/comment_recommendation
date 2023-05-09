def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = 0
    B = []
    for i in range(N-1, -1, -1):
        if sum(A[i::i+1]) % 2 != A[i]:
            M += 1
            B.append(i+1)
    print(M)
    for b in B:
        print(b)

if __name__ == '__main__':
    main()