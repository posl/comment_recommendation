def main():
    n, m = map(int, input().split())
    ab_list = []
    for i in range(m):
        a, b = map(int, input().split())
        ab_list.append([a, b])
    ab_list.sort(key=lambda x: x[1])
    # print(ab_list)
    ab_list.sort(key=lambda x: x[0])
    # print(ab_list)
    count = 0
    city = 1
    for i in range(m):
        if ab_list[i][0] == city:
            city = ab_list[i][1]
            count += 1
    print(count)
    return 0

if __name__ == '__main__':
    main()