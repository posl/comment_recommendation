def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.sort()
    x_list = [abs(x - i) for i in x_list]
    x_list = [i for i in x_list if i != 0]
    if len(x_list) == 0:
        print(0)
        return
    ans = x_list[0]
    for i in range(1, len(x_list)):
        ans = gcd(ans, x_list[i])
    print(ans)
