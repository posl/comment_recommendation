def main():
    N, M = map(int, input().split())
    k = []
    x = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])
    for i in range(N):
        for j in range(N):
            if i != j:
                if set(x[i]) & set(x[j]):
                    print('Yes')
                    return
    print('No')
