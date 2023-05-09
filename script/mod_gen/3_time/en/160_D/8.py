def getG(N):
    G = [[] for i in range(N)]
    for i in range(N-1):
        G[i].append(i+1)
        G[i+1].append(i)
    return G

if __name__ == '__main__':
    getG()