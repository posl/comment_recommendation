def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    d_list = []
    for i in range(n):
        d_list.append(x_list[i+1] - x_list[i])
    d = d_list[0]
    for i in range(n-1):
        d = gcd(d, d_list[i+1])
    print(d)
