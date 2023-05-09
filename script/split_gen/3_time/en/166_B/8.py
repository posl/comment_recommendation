def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(list(map(int, input().split())))
    print(N - sum(d[0][1:]))
