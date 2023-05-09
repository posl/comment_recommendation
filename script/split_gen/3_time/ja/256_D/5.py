def main():
    n = int(input())
    lr = [list(map(int, input().split())) for _ in range(n)]
    lr.sort(key=lambda x:x[0])
    l, r = lr[0][0], lr[0][1]
    for i in range(1, n):
        if lr[i][0] <= r:
            r = max(r, lr[i][1])
        else:
            print(l, r)
            l, r = lr[i][0], lr[i][1]
    print(l, r)
