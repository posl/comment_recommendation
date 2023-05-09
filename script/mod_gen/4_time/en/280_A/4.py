def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    print(sum([1 for i in range(h) for j in range(w) if s[i][j] == '#']))

if __name__ == '__main__':
    main()