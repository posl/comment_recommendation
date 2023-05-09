def main():
    s = input()
    q = int(input())
    t = [0]*q
    f = [0]*q
    c = [0]*q
    for i in range(q):
        t[i],f[i],c[i] = map(str,input().split())
    for i in range(q):
        if t[i] == '1':
            s = s[::-1]
        elif t[i] == '2':
            if f[i] == '1':
                s = c[i] + s
            elif f[i] == '2':
                s = s + c[i]
    print(s)
