def main():
    n, m, *a = map(int, open(0).read().split())
    a.sort(reverse = True)
    print("Yes" if a[m - 1] >= sum(a) / (4 * m) else "No")
main()

if __name__ == '__main__':
    main()