def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
            s[i] += '(' + str(d[s[i]]) + ')'
        else:
            d[s[i]] = 0
    for i in range(n):
        print(s[i])
