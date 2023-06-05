def main():
    n, q = map(int, input().split())
    s = input()
    ac = [0] * (n + 1)
    for i in range(1, n):
        if s[i - 1] == 'A' and s[i] == 'C':
            ac[i] = ac[i - 1] + 1
        else:
            ac[i] = ac[i - 1]
    for i in range(q):
        l, r = map(int, input().split())
        print(ac[r - 1] - ac[l - 1])

if __name__ == '__main__':
    main()