def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    for i in range(M):
        if A[i] == 1:
            if B[i] == N:
                print("POSSIBLE")
                return
    print("IMPOSSIBLE")

if __name__ == '__main__':
    main()