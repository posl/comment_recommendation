def main():
    n,m = map(int,input().split())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort()
    sum = 0
    for i in range(n):
        if m >= l[i][1]:
            sum += l[i][0] * l[i][1]
            m -= l[i][1]
        else:
            sum += l[i][0] * m
            break
    print(sum)
