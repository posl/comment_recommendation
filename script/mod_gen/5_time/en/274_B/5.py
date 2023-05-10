def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    for i in range(w):
        print(sum(c[j][i] == '#' for j in range(h)))

if __name__ == '__main__':
    main()