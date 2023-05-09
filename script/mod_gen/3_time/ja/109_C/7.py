def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    d_list = [x_list[i+1] - x_list[i] for i in range(n)]
    if n == 1:
        print(d_list[0])
    else:
        d = d_list[0]
        for i in range(n-1):
            d = min(d, d_list[i+1])
        print(d)

if __name__ == '__main__':
    main()