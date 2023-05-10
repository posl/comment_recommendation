def main():
    N,M,T = map(int,input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int,input().split())))
    AB = sorted(AB, key=lambda x:x[0])
    AB = sorted(AB, key=lambda x:x[1])
    #print(AB)
    if AB[0][0] > 0.5:
        print('No')
        exit()
    else:
        N = N - AB[0][1] + AB[0][0]
    #print(N)
    for i in range(1,M):
        #print(N)
        if N <= 0:
            print('No')
            exit()
        else:
            N = N - (AB[i][1] - AB[i][0])
            if N + 0.5 < AB[i][0]:
                print('No')
                exit()
            else:
                N = N + 0.5
    if N <= 0:
        print('No')
        exit()
    else:
        N = N - (T - AB[M-1][1])
        if N <= 0:
            print('No')
            exit()
        else:
            print('Yes')
            exit()
