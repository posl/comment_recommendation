def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [abs(a[i]) for i in range(n)]
    c = [a[i] for i in range(n) if a[i] < 0]
    if len(c) % 2 == 0:
        print(sum(b))
    else:
        print(sum(b) - 2 * min(b))

if __name__ == '__main__':
    main()