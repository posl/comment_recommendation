def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    s = set()
    for i in range(M):
        for j in range(M):
            if A[i] == B[j]:
                s.add(A[i])
    print(N - len(s))
    return

if __name__ == '__main__':
    main()