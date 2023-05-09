def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    d_list = []
    for i in range(1, len(x_list)):
        d_list.append(x_list[i] - x_list[i-1])
    d = d_list[0]
    for i in range(1, len(d_list)):
        d = gcd(d, d_list[i])
    print(d)
