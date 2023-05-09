def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_,t_ = input().split()
        s.append(s_)
        t.append(t_)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if s[i] == s[j] or t[i] == t[j]:
                print("No")
                return
    print("Yes")
