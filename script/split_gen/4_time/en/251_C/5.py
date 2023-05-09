def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        st = input().split()
        s.append(st[0])
        t.append(int(st[1]))
    max = 0
    for i in range(n):
        if t[i] > max:
            max = t[i]
            max_s = s[i]
    print(s.index(max_s) + 1)
