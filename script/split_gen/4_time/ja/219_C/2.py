def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    table = {}
    for i in range(len(x)):
        table[x[i]] = chr(ord('a') + i)
    for i in range(n):
        s[i] = s[i].translate(str.maketrans(table))
    s = sorted(s)
    for i in range(n):
        s[i] = s[i].translate(str.maketrans(dict(map(reversed, table.items()))))
    for i in range(n):
        print(s[i])
