def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - a[i - 1]
    b.pop(0)
    b.sort(reverse=True)
    print(sum(b[:n - m]))

if __name__ == '__main__':
    main()