def main():
    p = [int(x) for x in input().split()]
    s = [chr(97+i) for i in range(26)]
    t = [0]*26
    for i in range(26):
        t[p[i]-1] = s[i]
    print(''.join(t))

if __name__ == '__main__':
    main()