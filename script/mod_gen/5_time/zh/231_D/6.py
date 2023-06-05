def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    for i in range(M):
        if A[i] > B[i]:
            A[i], B[i] = B[i], A[i]
    for i in range(M - 1):
        if B[i] != A[i + 1]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()