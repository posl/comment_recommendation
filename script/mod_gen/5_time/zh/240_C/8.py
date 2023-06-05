def main():
    n, x = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1], reverse=True)
    for a, b in ab:
        if x == a or x == b:
            print('Yes')
            break
        elif x > a:
            x -= a
            x += b
        else:
            print('No')
            break
    else:
        print('No')

if __name__ == '__main__':
    main()