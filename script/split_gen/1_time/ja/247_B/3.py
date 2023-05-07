def main():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        si, ti = input().split()
        s.append(si)
        t.append(ti)
    for i in range(n):
        for j in range(n):
            if i != j and (s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]):
                print("No")
                return
    print("Yes")
    return
