def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    for i in range(N):
        for j in range(N):
            if i != j:
                if s[i] == s[j] or t[i] == t[j]:
                    print("No")
                    return
    print("Yes")
