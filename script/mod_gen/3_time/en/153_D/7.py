def main(h):
    #h = int(input())
    ans = 1
    while h > 1:
        h = h//2
        ans += h
    print(ans)

if __name__ == '__main__':
    main()