def main():
    n = int(input())
    a = []
    for i in range(n):
        l, r = map(int, input().split())
        a.append((l, r))
    a.sort(key=lambda x: x[0])
    ans = []
    for i in range(n):
        if len(ans) == 0:
            ans.append(a[i])
        else:
            if ans[-1][1] >= a[i][0]:
                ans[-1] = (ans[-1][0], max(ans[-1][1], a[i][1]))
            else:
                ans.append(a[i])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

if __name__ == '__main__':
    main()