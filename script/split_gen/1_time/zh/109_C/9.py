def main():
    N, X = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(X)
    x_list.sort()
    d_list = []
    for i in range(N):
        d_list.append(x_list[i + 1] - x_list[i])
    gcd = d_list[0]
    for i in range(N - 1):
        gcd = calc_gcd(gcd, d_list[i + 1])
    print(gcd)
