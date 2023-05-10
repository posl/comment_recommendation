def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    c = [list(map(int, input().split())) for _ in range(m)]
    if m == 0:
        print("Yes")
        return
    a.sort()
    c.sort()
    for i in range(m):
        if a[i][1] != c[i][1]:
            print("No")
            return
    print("Yes")
main()

if __name__ == '__main__':
    main()