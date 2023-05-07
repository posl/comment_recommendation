def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    s = [sum(p[i]) for i in range(n)]
    for i in range(n):
        s[i] += 300 * (k - 1)
        if s[i] > sum(p[i]) + 300 * (k - 1):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()