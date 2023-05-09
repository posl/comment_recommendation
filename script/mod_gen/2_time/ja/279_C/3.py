def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    if sorted(s) == sorted(t):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()