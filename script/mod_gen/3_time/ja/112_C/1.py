def main():
    n = int(input())
    x_list = []
    y_list = []
    h_list = []
    for i in range(n):
        x, y, h = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
        h_list.append(h)
    for cx in range(101):
        for cy in range(101):
            h = 0
            for i in range(n):
                if h_list[i] != 0:
                    tmp_h = h_list[i] + abs(x_list[i] - cx) + abs(y_list[i] - cy)
                    if h == 0:
                        h = tmp_h
                    elif h != tmp_h:
                        h = -1
                        break
            if h != -1:
                print(cx, cy, h)
                return

if __name__ == '__main__':
    main()