def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    print("Yes" if len(set(a)) + len(set(b)) == n + 1 else "No")

if __name__ == '__main__':
    main()