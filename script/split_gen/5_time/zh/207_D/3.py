def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        x,y = map(int,input().split())
        s.append([x,y])
    for i in range(n):
        x,y = map(int,input().split())
        t.append([x,y])
    s.sort()
    t.sort()
    s = [s[i][0] for i in range(n)]
    t = [t[i][0] for i in range(n)]
    if s == t:
        print('Yes')
    else:
        print('No')
