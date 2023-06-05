def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if i == 0:
            print(s[i])
        elif s[i] in s[:i]:
            print(s[i] + "(" + str(s[:i].count(s[i])) + ")")
        else:
            print(s[i])
