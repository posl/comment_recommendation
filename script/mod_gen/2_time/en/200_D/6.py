def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = 200
    r = [None] * m
    for i in range(n):
        b = a[i] % m
        if r[b] is None:
            r[b] = [i]
        else:
            print("Yes")
            print(1, r[b][0] + 1)
            print(1, i + 1)
            return
    for i in range(m):
        if r[i] is not None and len(r[i]) == 2:
            print("Yes")
            print(2, r[i][0] + 1, r[i][1] + 1)
            return
    print("No")

if __name__ == '__main__':
    main()