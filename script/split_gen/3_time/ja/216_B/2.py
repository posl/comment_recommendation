def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = input().split()
        s.append(a)
        t.append(b)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j] and t[i] == t[j]:
                print("Yes")
                exit()
    print("No")
