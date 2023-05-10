def main():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    for i in range(n):
        p[i].sort(reverse=True)
    for i in range(n):
        p[i] = sum(p[i][:k])
    for i in range(n):
        if p[i] >= sum(p[:k]):
            print('Yes')
        else:
            print('No')
