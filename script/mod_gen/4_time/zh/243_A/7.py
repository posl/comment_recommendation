def main():
    v, a, b, c = map(int, input().split())
    while v:
        if v < a:
            print('F')
            break
        elif v < b:
            print('M')
            break
        elif v < c:
            print('T')
            break
        else:
            v -= a
            v -= b
            v -= c

if __name__ == '__main__':
    main()