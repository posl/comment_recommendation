def main():
    n = int(input())
    c = input()
    r = 0
    w = 0
    for i in c:
        if i == 'R':
            r += 1
        else:
            w += 1
    if r == 0 or w == 0:
        print(0)
    elif c[0] == 'R' and c[-1] == 'R':
        print(w)
    elif c[0] == 'W' and c[-1] == 'W':
        print(r)
    else:
        print(1)
