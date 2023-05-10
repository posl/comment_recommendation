def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    x = list(x)
    y = []
    for i in range(26):
        y.append(chr(ord('a') + i))
    d = {}
    for i in range(26):
        d[y[i]] = x[i]
    for i in range(n):
        s[i] = list(s[i])
        for j in range(len(s[i])):
            s[i][j] = d[s[i][j]]
        s[i] = ''.join(s[i])
    s.sort()
    for i in range(n):
        for j in range(len(s[i])):
            s[i][j] = d[s[i][j]]
        s[i] = ''.join(s[i])
    for i in range(n):
        print(s[i])
