def solv():
    n = int(input())
    x_list = []
    y_list = []
    for i in range(n):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
    x_list.sort()
    y_list.sort()
    x_dict = {}
    y_dict = {}
    for i in range(n):
        x_dict[x_list[i]] = i
        y_dict[y_list[i]] = i
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1 = x_list[i]
            x2 = x_list[j]
            y1 = y_list[i]
            y2 = y_list[j]
            if (x1, y2) in x_dict and (x2, y1) in x_dict:
                ans += 1
    print(ans)
