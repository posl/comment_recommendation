def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    print(sum([si.count('#') for si in s]))

if __name__ == '__main__':
    main()