def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        st = input().split()
        s.append(st[0])
        t.append(st[1])
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                print("No")
                return
            if t[i] == t[j]:
                print("No")
                return
    print("Yes")
