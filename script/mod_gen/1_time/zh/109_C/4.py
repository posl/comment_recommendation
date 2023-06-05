def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    if n == 1:
        print(x_list[1] - x_list[0])
    else:
        x_list_diff = [x_list[i+1] - x_list[i] for i in range(n)]
        x_list_diff.sort()
        print(x_list_diff[0])

if __name__ == '__main__':
    main()