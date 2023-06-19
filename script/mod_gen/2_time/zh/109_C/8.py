def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    diff_list = [abs(x_list[i] - x_list[i+1]) for i in range(n)]
    print(gcd_list(diff_list))

if __name__ == '__main__':
    main()