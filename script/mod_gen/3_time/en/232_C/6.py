def main():
    N,M = map(int,input().split())
    A = []
    for i in range(M):
        A.append(list(map(int,input().split())))
    C = []
    for i in range(M):
        C.append(list(map(int,input().split())))
    def check(A,C):
        for i in range(len(A)):
            if A[i] in C:
                pass
            else:
                return False
        return True
    for i in range(N):
        A1 = [A[j] for j in range(M) if A[j][0] == i+1]
        C1 = [C[j] for j in range(M) if C[j][0] == i+1]
        if check(A1,C1):
            pass
        else:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()