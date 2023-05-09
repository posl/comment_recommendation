def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        tmp = input().split()
        s.append(tmp[0])
        t.append(tmp[1])
    for i in range(n):
        if s[i] in t:
            print("No")
            exit(0)
    print("Yes")
