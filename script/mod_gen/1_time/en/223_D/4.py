def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #入力の検証
    for i in range(M):
        if A[i] == B[i]:
            print(-1)
            return
    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == A[j] and B[i] == B[j]:
                print(-1)
                return
    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == B[j] and B[i] == A[j]:
                print(-1)
                return
    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == B[j] and B[i] == B[j]:
                print(-1)
                return
    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == A[j] and B[i] == A[j]:
                print(-1)
                return
    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == B[j] and B[i] == B[j]:
                print(-1)
                return
    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == A[j] and B[i] == B[j]:
                print(-1)
                return
    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == B[j] and B[i] == A[j]:
                print(-1)
                return
    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == B

if __name__ == '__main__':
    main()