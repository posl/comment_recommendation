def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    bc = [list(map(int, input().split())) for _ in range(m)]
    bc.sort(key=lambda x: x[1], reverse=True)
    idx = 0
    for b, c in bc:
        for _ in range(b):
            if idx >= n or c <= a[idx]:
                break
            a[idx] = c
            idx += 1
    print(sum(a))

if __name__ == '__main__':
    main()