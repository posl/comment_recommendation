def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in bc:
        while b > 0 and i < n and a[i] < c:
            a[i] = c
            i += 1
            b -= 1
        if b == 0:
            break
    print(sum(a))

if __name__ == '__main__':
    main()