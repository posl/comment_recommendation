def main():
    v,a,b,c = map(int, input().split())
    v -= a
    if v <= 0:
        print('F')
        return
    v -= b
    if v <= 0:
        print('M')
        return
    v -= c
    if v <= 0:
        print('T')
        return

if __name__ == '__main__':
    main()