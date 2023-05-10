def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    a.append(a[1])
    s = sum(a)
    mx = 0
    for i in range(n):
        mx = max(mx, s - a[i] - a[i + 1] - a[i + 2])
    print(mx)

if __name__ == '__main__':
    main()