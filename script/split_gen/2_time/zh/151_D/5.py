def main():
    n,m = map(int,input().split())
    p = [0 for i in range(n)]
    s = ["" for i in range(n)]
    for i in range(m):
        p[i],s[i] = input().split()
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == "AC":
            ac += 1
        else:
            wa += 1
    print(ac,wa)
