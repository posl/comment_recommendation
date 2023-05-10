def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.append(t[i])
    for i in range(n):
        if i == 0:
            continue
        if ans[i] > ans[i-1] + s[i-1]:
            ans[i] = ans[i-1] + s[i-1]
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()