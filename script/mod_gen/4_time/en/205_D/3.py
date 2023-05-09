def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    for i in range(q):
        l, r = 0, 10 ** 18
        while r - l > 1:
            m = (l + r) // 2
            if sum(m // ai for ai in a) < k[i]:
                l = m
            else:
                r = m
        print(r)

if __name__ == '__main__':
    main()