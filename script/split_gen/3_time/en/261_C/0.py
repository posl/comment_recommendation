def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 0
            print(s[i])
        else:
            d[s[i]] += 1
            print(s[i] + "(" + str(d[s[i]]) + ")")
