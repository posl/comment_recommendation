def main():
    n, w = map(int, input().split())
    a = []
    for i in range(n):
        s, t, p = map(int, input().split())
        a.append((s, p))
        a.append((t, -p))
    a.sort()
    s = 0
    for _, p in a:
        s += p
        if s > w:
            print("No")
            break
    else:
        print("Yes")

if __name__ == '__main__':
    main()