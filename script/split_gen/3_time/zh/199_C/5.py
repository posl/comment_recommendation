def main():
    n = int(input())
    s = input()
    q = int(input())
    t = []
    a = []
    b = []
    for i in range(q):
        t_i, a_i, b_i = map(int, input().split())
        t.append(t_i)
        a.append(a_i)
        b.append(b_i)
    for i in range(q):
        if t[i] == 1:
            s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        elif t[i] == 2:
            s = s[n:] + s[:n]
    print(s)
