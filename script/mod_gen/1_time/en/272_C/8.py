def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    # compute
    A.sort()
    A.reverse()
    B = []
    for i in range(N-1):
        for j in range(i+1, N):
            if (A[i] + A[j]) % 2 == 0:
                B.append(A[i] + A[j])
    if len(B) == 0:
        print(-1)
    else:
        print(max(B))

if __name__ == '__main__':
    main()