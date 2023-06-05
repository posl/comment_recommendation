def main():
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    count = 0
    for i in range(N):
        flag = 0
        for j in range(M):
            if i+1 == A[j]:
                if H[i] <= H[B[j]-1]:
                    flag = 1
                    break
            elif i+1 == B[j]:
                if H[i] <= H[A[j]-1]:
                    flag = 1
                    break
        if flag == 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()