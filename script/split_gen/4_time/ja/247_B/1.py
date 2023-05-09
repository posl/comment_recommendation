def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        si, ti = input().split()
        s.append(si)
        t.append(ti)
    for i in range(n):
        if s[i] in t:
            if s[i] != t[i]:
                print("Yes")
                exit()
    print("No")
