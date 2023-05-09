def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = []
    D = []
    for j in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    if N == 1:
        print("Yes")
        return
    for i in range(0, N):
        for j in range(0, N):
            if i != j:
                if A.count(i+1) == C.count(j+1) and B.count(i+1) == D.count(j+1):
                    continue
                else:
                    print("No")
                    return
    print("Yes")

if __name__ == '__main__':
    main()