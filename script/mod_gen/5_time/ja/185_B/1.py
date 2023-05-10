def main():
    N,M,T = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    flag = True
    battery = N
    for i in range(M):
        if flag == False:
            break
        battery -= (A[i] - B[i-1])
        if battery <= 0:
            flag = False
            break
        battery += (B[i] - A[i])
        if battery > N:
            battery = N
    battery -= (T - B[M-1])
    if battery <= 0:
        flag = False
    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()