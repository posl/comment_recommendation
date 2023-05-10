def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = "Yes"
    for i in range(n):
        if a[i] != i+1:
            ans = "No"
            break
    print(ans)

if __name__ == '__main__':
    main()