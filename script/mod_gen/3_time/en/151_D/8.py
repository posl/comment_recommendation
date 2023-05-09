def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    print(h*w - sum([s[i].count('#') for i in range(h)]))

if __name__ == '__main__':
    main()