def main():
    N = int(input())
    a = list(map(int, input().split()))
    m = []
    for i in range(N):
        for j in range(i, N):
            m.append(a[i:j + 1])
    ans = []
    for i in m:
        i.sort()
        ans.append(i[len(i) // 2])
    ans.sort()
    print(ans[len(ans) // 2])

if __name__ == '__main__':
    main()