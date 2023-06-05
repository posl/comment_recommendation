def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if i == 0:
            ans.append(1)
        else:
            ans.append(ans[i - 1] + 1)
        for j in range(i - 1, -1, -1):
            if a[i] == a[j]:
                ans[i] = ans[j]
                break
            elif a[i] < a[j]:
                ans[i] = ans[j] + 1
                break
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()