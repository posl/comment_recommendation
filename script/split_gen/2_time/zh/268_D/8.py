def main():
    n,m = map(int,input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                print(-1)
                exit()
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                print(-1)
                exit()
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                print(-1)
                exit()
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                print(-1)
                exit()
    print(s[0],end = '')
    for i in range(1,n):
        print('_',end = '')
        print(s[i],end = '')
    print()
    print(t[0],end = '')
    for i in range(1,m):
        print('_',end = '')
        print(t[i],end = '')
    print()
