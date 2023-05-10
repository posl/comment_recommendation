def main():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    for i in range(n):
        p[i].append(sum(p[i]))
    p.sort(key=lambda x: x[3], reverse=True)
    for i in range(n):
        if i < k:
            print('Yes')
        else:
            print('No')
