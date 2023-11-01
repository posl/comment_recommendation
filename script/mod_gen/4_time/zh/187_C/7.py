def main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = set()
    for i in range(n):
        if s[i][0] == '!':
            t.add(s[i])
        else:
            t.add('

if __name__ == '__main__':
    main()