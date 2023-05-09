def main():
    n, s, d = map(int, input().split())
    xy = [list(map(int, input().split())) for i in range(n)]
    for i in range(n):
        if xy[i][0] < s and xy[i][1] > d:
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()