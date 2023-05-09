def main():
    N, X = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(X)
    x_list.sort()
    diff_list = []
    for i in range(1, N+1):
        diff_list.append(x_list[i]-x_list[i-1])
    ans = diff_list[0]
    for i in range(1, len(diff_list)):
        ans = gcd(ans, diff_list[i])
    print(ans)

if __name__ == '__main__':
    main()