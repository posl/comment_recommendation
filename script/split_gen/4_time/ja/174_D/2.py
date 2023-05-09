def main():
    N = int(input())
    C = input()
    r = 0
    w = 0
    for c in C:
        if c == 'R':
            r += 1
        else:
            w += 1
    if r == 0 or w == 0:
        print(0)
        return
    if C[0] == 'W':
        w -= 1
    if C[-1] == 'R':
        r -= 1
    print(min(r, w))
