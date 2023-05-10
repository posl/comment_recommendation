def main():
    n, m = map(int, input().split())
    k = []
    x = []
    for i in range(m):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])
    print('Yes' if len(set(x[0]) & set(x[1])) > 0 else 'No')
