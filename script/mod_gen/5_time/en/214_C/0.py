def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    ans[0] = t[0]
    for i in range(1, n):
        ans[i] = min(t[i], ans[i-1] + s[i-1])
    for i in range(n):
        print(ans[i])
    return

if __name__ == '__main__':
    main()