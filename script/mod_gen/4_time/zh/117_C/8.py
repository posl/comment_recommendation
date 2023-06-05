def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    if n == 1:
        print(min([abs(i - x[0]) for i in x]))
        return
    d = [x[i + 1] - x[i] for i in range(m - 1)]
    d.sort(reverse=True)
    print(x[-1] - x[0] - sum(d[:n - 1]))
    return

if __name__ == '__main__':
    main()