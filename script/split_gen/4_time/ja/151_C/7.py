def main():
    n,m = map(int,input().split())
    p = [0 for i in range(n)]
    s = ["" for i in range(n)]
    for i in range(m):
        p_temp,s_temp = input().split()
        p_temp = int(p_temp)
        p[p_temp-1] += 1
        s[p_temp-1] = s_temp
    ac = 0
    wa = 0
    for i in range(n):
        if p[i] != 0:
            ac += 1
            if s[i] == "WA":
                wa += p[i] - 1
    print(ac,wa)
