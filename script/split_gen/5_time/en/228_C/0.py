def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    for i in range(N):
        P[i].append(sum(P[i]))
    P.sort(key=lambda x:x[3], reverse=True)
    for i in range(N):
        if i < K:
            print('Yes')
        else:
            print('No')
