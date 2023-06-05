def main():
    n = int(input())
    a = []
    for i in range(n):
        l, r = map(int, input().split())
        a.append([l, r])
    a.sort(key=lambda x: x[0])
    ans = [[a[0][0], a[0][1]]]
    for i in range(1, n):
        if ans[-1][1] < a[i][0]:
            ans.append([a[i][0], a[i][1]])
        else:
            ans[-1][1] = max(ans[-1][1], a[i][1])
    for i in ans:
        print(i[0], i[1])

if __name__ == '__main__':
    main()