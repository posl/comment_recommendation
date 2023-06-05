def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    n += 1
    diff_list = [x_list[i+1] - x_list[i] for i in range(0, n-1)]
    gcd = diff_list[0]
    for i in range(1, n-1):
        gcd = get_gcd(gcd, diff_list[i])
    print(gcd)
