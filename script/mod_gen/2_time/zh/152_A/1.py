def main():
    h, w = map(int, input().split())
    s = [[c for c in input()] for _ in range(h)]
    ans = 0
    for si in s:
        ans += si.count('.')
    print(ans - 1)

if __name__ == '__main__':
    main()