def main():
    n, w = map(int, input().split())
    a = [0] * 200010
    for i in range(n):
        s, t, p = map(int, input().split())
        a[s] += p
        a[t] -= p
    for i in range(1, 200010):
        a[i] += a[i - 1]
        if a[i] > w:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()