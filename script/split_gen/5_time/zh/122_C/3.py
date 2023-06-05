def main():
    n, q = map(int, input().split())
    s = input()
    l = []
    r = []
    for i in range(q):
        l1, r1 = map(int, input().split())
        l.append(l1)
        r.append(r1)
    for i in range(q):
        print(s[l[i]-1:r[i]].count("AC"))
