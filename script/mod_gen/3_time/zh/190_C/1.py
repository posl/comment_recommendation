def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    K = int(input())
    C = []
    D = []
    for i in range(K):
        c,d = map(int,input().split())
        C.append(c)
        D.append(d)
    maxCount = 0
    for i in range(2**K):
        ball = [0]*N
        count = 0
        for j in range(K):
            if ((i>>j)&1):
                ball[D[j]-1] += 1
            else:
                ball[C[j]-1] += 1
        for j in range(M):
            if ball[A[j]-1] > 0 and ball[B[j]-1] > 0:
                count += 1
        if count > maxCount:
            maxCount = count
    print(maxCount)

if __name__ == '__main__':
    main()