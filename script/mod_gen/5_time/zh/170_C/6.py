def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
    else:
        p = list(map(int, input().split()))
        p.sort()
        i = 0
        j = 0
        while i < len(p):
            if p[i] == x:
                p.pop(i)
                i -= 1
            i += 1
        while True:
            if x - j not in p:
                print(x - j)
                break
            elif x + j not in p:
                print(x + j)
                break
            j += 1

if __name__ == '__main__':
    main()