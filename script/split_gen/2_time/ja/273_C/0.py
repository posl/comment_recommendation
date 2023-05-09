def main():
    n = int(input())
    a = list(map(int,input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    l = sorted(d.items(), key=lambda x:x[1], reverse=True)
    s = 0
    for i in range(n):
        if l[i][1] == 1:
            break
        s += 1
    for i in range(n):
        if l[i][1] == 1:
            print(s)
        else:
            print(s+1)
