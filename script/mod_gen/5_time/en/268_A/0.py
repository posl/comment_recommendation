def main():
    a, b, c, d, e = map(int, input().split())
    ans = len(set([a, b, c, d, e]))
    print(ans)

if __name__ == '__main__':
    main()