def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    x_diff = [x_list[i+1] - x_list[i] for i in range(n)]
    x_diff_min = min(x_diff)
    ans = x_diff_min
    for x_diff_i in x_diff:
        ans = gcd(ans, x_diff_i)
    print(ans)
