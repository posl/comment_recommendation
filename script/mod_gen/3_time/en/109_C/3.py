def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    if n == 1:
        print(x_list[1] - x_list[0])
    else:
        d_list = []
        for i in range(n):
            d_list.append(x_list[i+1] - x_list[i])
        import math
        d = math.gcd(d_list[0], d_list[1])
        for i in range(n-2):
            d = math.gcd(d, d_list[i+2])
        print(d)

if __name__ == '__main__':
    main()