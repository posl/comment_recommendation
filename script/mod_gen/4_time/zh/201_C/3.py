def main():
    s = input()
    o = s.count('o')
    x = s.count('x')
    q = s.count('?')
    ans = 0
    if o > 4:
        ans = 0
    elif o == 4:
        ans = 24
    elif o == 3:
        ans = 36
    elif o == 2:
        ans = 14
    elif o == 1:
        ans = 1
    elif o == 0:
        ans = 0
    print(ans)

if __name__ == '__main__':
    main()