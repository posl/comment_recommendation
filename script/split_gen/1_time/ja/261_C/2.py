def main():
    n = int(input())
    s = [input() for i in range(n)]
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 1
            print(s[i])
        else:
            print(s[i] + "(" + str(d[s[i]]) + ")")
            d[s[i]] += 1
