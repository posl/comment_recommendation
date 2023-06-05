def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[i] = t[i]
        else:
            ans[i] = min(ans[i-1] + s[i-1], t[i])
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()