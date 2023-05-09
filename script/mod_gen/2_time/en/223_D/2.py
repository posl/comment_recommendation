def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    if 1 in a:
        print(-1)
    else:
        print(1)
    return

if __name__ == '__main__':
    main()