def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    diff_list = []
    for i in range(n):
        diff_list.append(x_list[i + 1] - x_list[i])
    diff_list.sort()
    if n == 1:
        print(diff_list[0])
    else:
        print(gcd(diff_list[0], diff_list[1]))

if __name__ == '__main__':
    main()