def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    a = [x for x in a if x != ['.'] * W]
    a = [x for x in zip(*a) if x != ['.'] * len(a)]
    a = [list(x) for x in zip(*a)]
    for x in a:
        print(''.join(x))

if __name__ == '__main__':
    main()