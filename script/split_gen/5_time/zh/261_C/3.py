def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
            s[i] = s[i] + '(' + str(d[s[i]]) + ')'
        else:
            d[s[i]] = 0
    for i in range(n):
        print(s[i])
