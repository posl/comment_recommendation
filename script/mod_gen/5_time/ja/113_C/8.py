def main():
    N,M = map(int,input().split())
    PY = [list(map(int,input().split())) for i in range(M)]
    dic = {}
    for i in range(1,N+1):
        dic[i] = []
    for i in range(M):
        dic[PY[i][0]].append(PY[i][1])
    for i in range(1,N+1):
        dic[i].sort()
    for i in range(M):
        print(str(PY[i][0]).zfill(6)+str(dic[PY[i][0]].index(PY[i][1])+1).zfill(6))

if __name__ == '__main__':
    main()