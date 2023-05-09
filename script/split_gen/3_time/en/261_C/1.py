def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 0
            print(s[i])
        else:
            d[s[i]] += 1
            print(s[i] + '({})'.format(d[s[i]]))
    return
