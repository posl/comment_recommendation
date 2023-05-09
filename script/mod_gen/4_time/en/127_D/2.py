def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = [list(map(int, input().split())) for _ in range(m)]
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in bc:
        for _ in range(b):
            if i >= n or c <= a[i]:
                break
            a[i] = c
            i += 1
        if i >= n:
            break
    print(sum(a))

if __name__ == '__main__':
    main()