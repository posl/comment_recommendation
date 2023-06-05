def main():
    n, q = map(int, input().split())
    s = input()
    ac = [0] * (n + 1)
    for i in range(n):
        ac[i + 1] = ac[i]
        if s[i:i + 2] == 'AC':
            ac[i + 1] += 1
    for _ in range(q):
        l, r = map(int, input().split())
        print(ac[r - 1] - ac[l - 1])

if __name__ == '__main__':
    main()