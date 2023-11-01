def main():
    n = int(input())
    s = input()
    r, g, b = 0, 0, 0
    for i in range(n):
        if s[i] == 'R':
            r += 1
        elif s[i] == 'G':
            g += 1
        else:
            b += 1
    ans = r * g * b
    for i in

if __name__ == '__main__':
    main()