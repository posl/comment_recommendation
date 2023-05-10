def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a,b = input().split()
        s.append(a)
        t.append(b)
    for i in range(n):
        if s[i] == t[i]:
            print("No")
            return
        if s[i] in t[i+1:]:
            print("No")
            return
    print("Yes")
    return
