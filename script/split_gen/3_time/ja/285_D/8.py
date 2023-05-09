def main():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        s_, t_ = input().split()
        s.append(s_)
        t.append(t_)
    for i in range(n):
        if s[i] == t[i]:
            print("No")
            return
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == t[j] and s[j] == t[i]:
                print("No")
                return
    print("Yes")
    return
