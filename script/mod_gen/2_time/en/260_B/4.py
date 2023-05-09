def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append((a[i], b[i], i + 1))
    c.sort(reverse = True)
    d = c[:x]
    c = c[x:]
    d.sort(key = lambda x: x[1], reverse = True)
    d += c[:y]
    c = c[y:]
    d.sort(key = lambda x: x[0] + x[1], reverse = True)
    d += c[:z]
    d.sort(key = lambda x: x[2])
    for i in d:
        print(i[2])

if __name__ == '__main__':
    main()