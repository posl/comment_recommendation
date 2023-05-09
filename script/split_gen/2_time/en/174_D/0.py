def main():
    n = int(input())
    c = input()
    r = 0
    w = 0
    for i in range(n):
        if c[i] == 'R':
            r += 1
    for i in range(r):
        if c[i] == 'W':
            w += 1
    print(w)
