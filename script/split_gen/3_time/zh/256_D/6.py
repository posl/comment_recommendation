def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort()
    x = l[0][0]
    y = l[0][1]
    for i in range(1, n):
        if y < l[i][0]:
            print(x, y)
            x = l[i][0]
            y = l[i][1]
        elif y < l[i][1]:
            y = l[i][1]
    print(x, y)
