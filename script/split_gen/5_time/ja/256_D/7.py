def main():
    n = int(input())
    lr = []
    for _ in range(n):
        l, r = map(int, input().split())
        lr.append((l, r))
    lr.sort()
    l, r = lr[0]
    for i in range(1, n):
        if lr[i][0] <= r:
            r = max(r, lr[i][1])
        else:
            print(l, r)
            l, r = lr[i]
    print(l, r)
