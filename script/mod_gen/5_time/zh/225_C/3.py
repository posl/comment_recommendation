def main():
    N, M = map(int, input().split())
    B = []
    for i in range(N):
        B.append(list(map(int, input().split())))
    #print(N, M)
    #print(B)
    for i in range(10**100):
        if i+M-1 > 10**100:
            break
        for j in range(7):
            if j+N-1 > 7:
                break
            A = []
            for k in range(N):
                A.append([(i+k)*7+l for l in range(j, j+M)])
            #print(A)
            if A == B:
                print('Yes')
                return
    print('No')
main()
