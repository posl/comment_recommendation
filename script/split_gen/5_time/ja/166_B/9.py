def main():
    n, k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    print(n - len(set([a[j][i] for j in range(k) for i in range(d[j])])))
