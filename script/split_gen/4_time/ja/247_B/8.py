def main():
    N = int(input())
    s = []
    t = []
    for i in range(0, N):
        s_t = input().split()
        s.append(s_t[0])
        t.append(s_t[1])
    for i in range(0, N):
        for j in range(0, N):
            if i != j:
                if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                    print("Yes")
                    return
    print("No")
