def main():
    N,K = map(int,input().split())
    data = []
    for i in range(N):
        data.append(list(map(int,input().split())))
    data.sort(key=lambda x:sum(x),reverse=True)
    for i in range(N):
        if sum(data[i]) + sum(data[K-1]) < sum(data[K]):
            print('No')
        else:
            print('Yes')
