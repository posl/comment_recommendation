def main():
    n, w = map(int, input().split())
    s = [0] * (2 * 10 ** 5 + 1)
    for _ in range(n):
        l, r, p = map(int, input().split())
        s[l] += p
        s[r] -= p
    for i in range(1, 2 * 10 ** 5 + 1):
        s[i] += s[i - 1]
        if s[i] > w:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()