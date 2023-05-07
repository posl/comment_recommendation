def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n - m + 1):
        b.append(sum(a[i:i + m]))
    print(sum(sorted(b, reverse=True)[:m]))

if __name__ == '__main__':
    main()