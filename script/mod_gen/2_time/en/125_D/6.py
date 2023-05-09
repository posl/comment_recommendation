def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += abs(a[i])
    if n%2==0:
        print(ans)
    else:
        print(ans-2*min(abs(a[i]) for i in range(n)))
main()

if __name__ == '__main__':
    main()