def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_, t_ = input().split()
        s.append(s_)
        t.append(t_)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                print("No")
                return
    print("Yes")
