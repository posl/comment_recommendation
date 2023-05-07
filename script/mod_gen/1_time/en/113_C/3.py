def main():
    #input
    N, M = map(int, input().split())
    P, Y = [], []
    for _ in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    #compute
    ans = [0]*M
    for i in range(N):
        p = i+1
        dic = {}
        for j in range(M):
            if P[j] == p:
                y = Y[j]
                if y in dic:
                    dic[y] += 1
                else:
                    dic[y] = 1
        for j in range(M):
            if P[j] == p:
                y = Y[j]
                ans[j] = str(p).zfill(6) + str(dic[y]).zfill(6)
                dic[y] -= 1
    #output
    for i in range(M):
        print(ans[i])

if __name__ == '__main__':
    main()