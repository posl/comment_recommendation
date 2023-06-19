def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.append(i + 1)
        if a[i] == ans[-2]:
            ans.pop()
            ans.pop()
    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()