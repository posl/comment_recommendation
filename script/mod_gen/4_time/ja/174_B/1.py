def main():
    n, d = map(int, input().split())
    x_list = []
    y_list = []
    for i in range(n):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
    cnt = 0
    for i in range(n):
        if x_list[i]**2 + y_list[i]**2 <= d**2:
            cnt += 1
    print(cnt)
main()
