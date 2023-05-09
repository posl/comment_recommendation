def getWV(N):
    wv = []
    for i in range(N):
        w, v = map(int, input().split())
        wv.append((w, v))
    return wv

if __name__ == '__main__':
    getWV()