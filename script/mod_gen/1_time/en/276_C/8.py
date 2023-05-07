def main():
    N = int(input())
    P = list(map(int, input().split()))
    A = [i for i in range(1, N+1)]
    Q = []
    for i in range(N):
        for j in range(N):
            if P[i] == A[j]:
                Q.append(j+1)
    print(*Q)

if __name__ == '__main__':
    main()