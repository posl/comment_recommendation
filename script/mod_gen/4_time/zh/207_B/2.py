def main():
    a, b, c, d = map(int, input().split())
    if a < b:
        print(-1)
        return
    if d == 1:
        print(0)
        return
    if b >= c * d:
        print(-1)
        return
    t = a // (c * d - b)
    if a % (c * d - b) == 0:
        print(t)
    else:
        print(t + 1)

if __name__ == '__main__':
    main()