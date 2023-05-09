def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a = input().split()
        s.append(a[0])
        t.append(a[1])
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j] and t[i] == t[j]:
                print("Yes")
                return
    print("No")
