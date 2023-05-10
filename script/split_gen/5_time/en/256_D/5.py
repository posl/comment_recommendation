def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l = sorted(l, key=lambda x: x[0])
    l = sorted(l, key=lambda x: x[1])
    x = l[0][0]
    y = l[0][1]
    for i in range(1, n):
        if l[i][0] <= y:
            y = max(y, l[i][1])
        else:
            print(x, y)
            x = l[i][0]
            y = l[i][1]
    print(x, y)
