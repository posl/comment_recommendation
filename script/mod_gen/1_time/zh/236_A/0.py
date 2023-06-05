def main():
    s = input()
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    s = list(s)
    s[a], s[b] = s[b], s[a]
    print(''.join(s))

if __name__ == '__main__':
    main()