def main():
    n,q = map(int,input().split())
    s = input()
    l = []
    r = []
    for i in range(q):
        l_i, r_i = map(int,input().split())
        l.append(l_i)
        r.append(r_i)
    for i in range(q):
        print(s[l[i]-1:r[i]-1].count('AC'))
