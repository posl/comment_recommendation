def main():
    n, m = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.sort()
    if n >= m:
        print(0)
        exit()
    diff_list = []
    for i in range(m-1):
        diff_list.append(x_list[i+1] - x_list[i])
    diff_list.sort()
    print(sum(diff_list[:m-n]))

if __name__ == '__main__':
    main()