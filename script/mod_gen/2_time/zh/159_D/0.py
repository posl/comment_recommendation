def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = [0] * n
    for i in range(n):
        ans[a[i]-1] += 1
    ans = [i*(i-1)//2 for i in ans]
    total = sum(ans)
    for i in range(n):
        print(total - ans[a[i]-1] + 1)

if __name__ == '__main__':
    main()