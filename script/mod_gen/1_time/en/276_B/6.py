def main():
    #input
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    #compute
    A = [[] for _ in range(N)]
    for a, b in AB:
        A[a-1].append(b)
        A[b-1].append(a)
    for i in range(N):
        A[i].sort()
        A[i] = [len(A[i])] + A[i]
    #output
    for a in A:
        print(*a)

if __name__ == '__main__':
    main()