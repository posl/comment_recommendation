def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    a = []
    for i in range(n):
        if s[i] in t:
            a.append(s[i])
        else:
            a.append(t[i])
    if len(a) == len(set(a)):
        print("Yes")
    else:
        print("No")
