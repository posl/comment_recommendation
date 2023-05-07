def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(N-M+1):
        B.append(sum(A[i:i+M]))
    print(max(B))

if __name__ == '__main__':
    main()