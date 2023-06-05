def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    out = [0] * n
    out[0] = 1
    for a, b in ab:
        if out[a - 1] == 1:
            out[b - 1] = a
        elif out[b - 1] == 1:
            out[a - 1] = b
    if 0 in out:
        print('No')
    else:
        print('Yes')
        for i in range(1, n):
            print(out[i])

if __name__ == '__main__':
    main()