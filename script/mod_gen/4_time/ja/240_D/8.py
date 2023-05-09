def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.append(1)
    ans.reverse()
    ans[0] = a[0]
    for i in range(1, n):
        if ans[i-1] == a[i]:
            ans[i] = 0
        else:
            ans[i] = a[i]
    ans.reverse()
    for i in range(n):
        if ans[i] == 0:
            ans[i] = ans[i-1]
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()