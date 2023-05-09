def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    s = input()
    l = []
    r = []
    for i in range(n):
        if s[i] == 'L':
            l.append(i)
        else:
            r.append(i)
    l.sort(key = lambda x: x)
    r.sort(key = lambda x: x)
    for i in range(len(l)):
        for j in range(len(r)):
            if x[l[i]] > x[r[j]] and y[l[i]] == y[r[j]]:
                print('Yes')
                return
    print('No')
    return
