def main():
    x, n = map(int, raw_input().split())
    p = map(int, raw_input().split())
    if n == 0:
        print x
        return
    p.sort()
    if x not in p:
        print x
        return
    for i in range(100):
        if x - i not in p:
            print x - i
            return
        if x + i not in p:
            print x + i
            return

if __name__ == '__main__':
    main()