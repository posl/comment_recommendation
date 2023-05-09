def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(list(map(int, input().split())))
    d = [j for i in d for j in i]
    d = set(d)
    print(N - len(d))
