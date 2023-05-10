def main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = {}
    for i in range(n):
        if s[i] in t:
            t[s[i]] += 1
            print(s[i] + "(" + str(t[s[i]]) + ")")
        else:
            t[s[i]] = 0
            print(s[i])
