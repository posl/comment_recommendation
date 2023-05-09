def main():
    from sys import stdin
    from itertools import groupby
    _ = int(stdin.readline())
    *H, = map(int, stdin.readline().split())
    print(max(len(list(g)) for k, g in groupby(H) if k < H[0]))

if __name__ == '__main__':
    main()