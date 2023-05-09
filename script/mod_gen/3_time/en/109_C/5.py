def main():
    N, X = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(X)
    x_list.sort()
    x_diff_list = [x_list[i+1] - x_list[i] for i in range(N)]
    gcd = x_diff_list[0]
    for i in range(1, N):
        gcd = gcd_calc(gcd, x_diff_list[i])
    print(gcd)

if __name__ == '__main__':
    main()