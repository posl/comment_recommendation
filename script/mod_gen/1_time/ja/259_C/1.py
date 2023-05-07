def main():
    s = input()
    t = input()
    p = 0
    for i in range(len(t)):
        if p < len(s) and s[p] == t[i]:
            p += 1
    print('Yes' if p == len(s) else 'No')

if __name__ == '__main__':
    main()