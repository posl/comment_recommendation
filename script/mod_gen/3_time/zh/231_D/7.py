def main():
    n, m = map(int, input().split())
    data = []
    for i in range(m):
        data.append(list(map(int, input().split())))
    data.sort(key=lambda x: x[1])
    # print(data)
    ans = "Yes"
    for i in range(m - 1):
        if data[i][1] == data[i + 1][0]:
            ans = "No"
            break
    print(ans)

if __name__ == '__main__':
    main()