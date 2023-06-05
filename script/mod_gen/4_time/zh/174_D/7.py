def solution():
    n = int(input())
    s = input()
    w = 0
    r = 0
    for i in range(n):
        if s[i] == 'W':
            w += 1
        else:
            r += 1
    if w == 0 or r == 0:
        print(0)
        return
    if s[0] == 'R' and s[-1] == 'R':
        print(r - 1)
        return
    if s[0] == 'W' and s[-1] == 'W':
        print(w - 1)
        return
    if s[0] == 'W' and s[-1] == 'R':
        print(r)
        return
    if s[0] == 'R' and s[-1] == 'W':
        print(r)
        return
    print(min(r, w))

if __name__ == '__main__':
    solution()