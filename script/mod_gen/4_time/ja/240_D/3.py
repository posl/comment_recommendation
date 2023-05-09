def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.append(0)
    for i in range(n):
        ans[a[i]-1] += 1
    for i in range(n):
        print(ans[i])
main()

if __name__ == '__main__':
    main()