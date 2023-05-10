def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        a[i] -= 1
        if i == 0:
            ans.append(1)
            continue
        if a[i] == a[i-1]:
            ans.append(ans[i-1]+1)
        else:
            ans.append(1)
    for j in ans:
        print(j)

if __name__ == '__main__':
    main()