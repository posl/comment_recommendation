def main():
    n, x = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    #print(n, x, ab)
    a = [i[0] for i in ab]
    b = [i[1] for i in ab]
    #print(a, b)
    if sum(a) + sum(b) <= x:
        print(2 * n)
        return
    elif sum(a) > x:
        print(0)
        return
    else:
        for i in range(n):
            if sum(a[:i+1]) + sum(b[:i+1]) > x:
                print(2 * i + 1)
                return
            elif sum(a[:i+1]) + sum(b[:i+1]) == x:
                print(2 * i + 2)
                return
            else:
                pass
        print(2 * n)

if __name__ == '__main__':
    main()