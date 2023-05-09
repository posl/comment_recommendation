def main():
    n = int(input())
    s = [input() for _ in range(n)]
    r = []
    for i in range(n):
        c = 0
        for j in range(i):
            if s[j] == s[i]:
                c += 1
        if c == 0:
            r.append(s[i])
        else:
            r.append(s[i] + "(" + str(c) + ")")
    for i in range(n):
        print(r[i])
