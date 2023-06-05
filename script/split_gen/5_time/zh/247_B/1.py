def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == s[j] or t[i] == t[j]:
                    print("Yes")
                    return
    print("No")
    return
