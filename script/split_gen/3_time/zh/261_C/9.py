def main():
    n = int(input())
    s = [input() for _ in range(n)]
    dict = {}
    for i in range(n):
        if s[i] in dict:
            dict[s[i]] += 1
            print(s[i] + '(' + str(dict[s[i]] - 1) + ')')
        else:
            dict[s[i]] = 1
            print(s[i])
