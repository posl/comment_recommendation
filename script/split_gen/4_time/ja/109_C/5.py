def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    x_diff_list = []
    for i in range(n):
        x_diff_list.append(x_list[i+1] - x_list[i])
    gcd = x_diff_list[0]
    for i in range(1, n):
        gcd = gcd_cal(gcd, x_diff_list[i])
    print(gcd)
