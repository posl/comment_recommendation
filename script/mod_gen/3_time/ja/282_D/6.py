def main():
    N, M = map(int, input().split())
    u = []
    v = []
    for i in range(M):
        u_i, v_i = map(int, input().split())
        u.append(u_i)
        v.append(v_i)
    #print(N, M)
    #print(u, v)
    #グラフGを作る
    G = [[] for i in range(N)]
    for i in range(M):
        G[u[i]-1].append(v[i]-1)
        G[v[i]-1].append(u[i]-1)
    #print(G)
    #print(len(G[0]))
    #print(len(G[4]))
    #print(len(G[2]))
    #print(len(G[1]))
    #print(len(G[3]))
    #print(len(G[5]))
    #print(len(G[6]))
    #print(len(G[7]))
    #print(len(G[8]))
    #print(len(G[9]))
    #print(len(G[10]))
    #print(len(G[11]))
    #print(len(G[12]))
    #print(len(G[13]))
    #print(len(G[14]))
    #print(len(G[15]))
    #print(len(G[16]))
    #print(len(G[17]))
    #print(len(G[18]))
    #print(len(G[19]))
    #print(len(G[20]))
    #print(len(G[21]))
    #print(len(G[22]))
    #print(len(G[23]))
    #print(len(G[24]))
    #print(len(G[25]))
    #print(len(G[26]))
    #print(len(G[27]))
    #print(len(G[28]))
    #print(len(G[29]))
    #print(len(G[30]))
    #print(len(G[31]))
    #print(len(G[32]))
    #print(len(G[33]))
    #print(len(G[34]))
    #print(len(G[35]))
    #print(len(G[36]))
    #print(len(G[37]))
    #print(len(G[38]))
    #print(len(G[39]))
    #print(len(G[40]))
    #print(len(G[41]))
    #print(len(G[42]))
    #print(len(G[43]))
    #print(len(G[44]))
    #print(len(G[45]))
    #print(len(G

if __name__ == '__main__':
    main()