def main():
    n, s, d = map(int, input().split())
    spells = [tuple(map(int, input().split())) for _ in range(n)]
    for x, y in spells:
        if x < s and y > d:
            print('Yes')
            break
    else:
        print('No')

if __name__ == '__main__':
    main()