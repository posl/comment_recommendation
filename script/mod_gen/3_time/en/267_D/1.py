def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] + (i + 1)
    b.sort(reverse=True)
    print(sum(b[:m]))

if __name__ == '__main__':
    main()