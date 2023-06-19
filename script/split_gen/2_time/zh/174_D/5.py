def main():
    n = int(input())
    s = input()
    r = 0
    w = 0
    for i in range(n):
        if s[i] == 'R':
            r += 1
    for i in range(r):
        if s[i] == 'W':
            w += 1
    print(w)
