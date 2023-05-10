def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for _ in range(N)]
    for i in range(N-1, -1, -1):
        if sum(B[i::i+1])%2 != A[i]:
            B[i] = 1
    print(sum(B))
    print(*[i+1 for i, b in enumerate(B) if b], sep='\n')

if __name__ == '__main__':
    main()