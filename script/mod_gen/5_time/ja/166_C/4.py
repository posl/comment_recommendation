def main():
    n, m = map(int, input().split())
    h_list = list(map(int, input().split()))
    ab_list = [list(map(int, input().split())) for _ in range(m)]
    max_h_list = [0] * n
    for ab in ab_list:
        a = ab[0] - 1
        b = ab[1] - 1
        max_h_list[a] = max(max_h_list[a], h_list[b])
        max_h_list[b] = max(max_h_list[b], h_list[a])
    ans = 0
    for i in range(n):
        if h_list[i] > max_h_list[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()