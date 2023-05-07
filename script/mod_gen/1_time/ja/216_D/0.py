def main():
    n, m = map(int, input().split())
    k = [0] * m
    a = [0] * m
    for i in range(m):
        k[i] = int(input())
        a[i] = list(map(int, input().split()))
    ball = [0] * (n + 1)
    for i in range(m):
        for j in range(k[i]):
            ball[a[i][j]] += 1
    for i in range(n + 1):
        if ball[i] % 2 != 0:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()