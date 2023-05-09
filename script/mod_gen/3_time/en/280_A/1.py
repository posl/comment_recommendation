def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    print(sum([s[i][j] == "#" for i in range(h) for j in range(w)]))

if __name__ == '__main__':
    main()