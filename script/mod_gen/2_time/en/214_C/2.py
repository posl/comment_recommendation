def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = t[i]
        t[(i+1) % n] = min(t[(i+1) % n], t[i]+s[i])
    print('
'.join(map(str, ans)))

if __name__ == '__main__':
    main()