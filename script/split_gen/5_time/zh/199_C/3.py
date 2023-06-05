def main():
    n = int(input())
    s = input()
    q = int(input())
    t = []
    a = []
    b = []
    for i in range(q):
        t_a_b = input()
        t_a_b = t_a_b.split()
        t.append(int(t_a_b[0]))
        a.append(int(t_a_b[1]))
        b.append(int(t_a_b[2]))
    for i in range(q):
        if t[i] == 1:
            s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        else:
            s = s[n:] + s[:n]
    print(s)
