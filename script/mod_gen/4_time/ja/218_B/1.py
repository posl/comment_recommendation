def main():
    p = list(map(int, input().split()))
    a = list(map(chr, range(97, 97+26)))
    for i in range(26):
        a[p[i]-1] = chr(97+i)
    print(''.join(a))

if __name__ == '__main__':
    main()