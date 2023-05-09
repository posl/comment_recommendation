def main():
    s = input()
    k = int(input())
    n = len(s)
    c = 0
    for i in range(n):
        if s[i] == 'X':
            c += 1
        else:
            break
    for i in reversed(range(n)):
        if s[i] == 'X':
            c += 1
        else:
            break
    if c == n:
        print(min(n, k + n))
    else:
        print(min(n, c + 2 * k))

if __name__ == '__main__':
    main()