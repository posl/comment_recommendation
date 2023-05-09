def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        name = input().split()
        s.append(name[0])
        t.append(name[1])
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                    print("Yes")
                    return
    print("No")
