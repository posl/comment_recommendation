def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0]*N
    for i in range(N):
        B[i] = A[i] ^ K
    #print(A)
    #print(B)
    #print(A+B)
    #print(set(A+B))
    #print(len(set(A+B)))
    print(max(A+B))

if __name__ == '__main__':
    main()