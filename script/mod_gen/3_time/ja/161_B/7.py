def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    ans = "No"
    if a[m-1] >= total/(4*m):
        ans = "Yes"
    print(ans)

if __name__ == '__main__':
    main()