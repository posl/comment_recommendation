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
            if s[i][-3:] == t[j]:
                print(i,j)
