def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.sort()
    diff_list = []
    for i in range(n-1):
        diff_list.append(x_list[i+1] - x_list[i])
    diff_list.sort()
    diff = diff_list[0]
    for i in range(n-1):
        diff = gcd(diff, diff_list[i])
    print(diff)

if __name__ == '__main__':
    main()