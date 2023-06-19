def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    diff_list = []
    for i in range(1, n+1):
        diff_list.append(x_list[i] - x_list[i-1])
    import math
    print(math.gcd(*diff_list))
