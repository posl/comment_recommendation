def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i] in s[:i]:
            x = 0
            for j in range(i):
                if s[j] == s[i]:
                    x += 1
            print(s[i] + '(' + str(x) + ')')
        else:
            print(s[i])
