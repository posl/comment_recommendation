def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    d_list = []
    for i in range(n):
        d_list.append(x_list[i+1] - x_list[i])
    d_list.sort()
    d = d_list[0]
    for i in range(n):
        d = gcd(d, d_list[i])
    print(d)

if __name__ == '__main__':
    main()