def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A[i] = i+1 の上司の番号
    # A[i] = i+1 の部下の数
    # A[i] = 1 の部下の数
    for i in range(N-1, 0, -1):
        A[A[i]-1] += A[i]
    for i in range(N):
        print(A[i])

if __name__ == '__main__':
    main()