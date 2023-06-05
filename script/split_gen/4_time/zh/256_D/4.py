def main():
    n = int(input())
    lr_list = []
    for i in range(n):
        lr_list.append(list(map(int, input().split())))
    lr_list.sort(key=lambda x: x[0])
    x = lr_list[0][0]
    y = lr_list[0][1]
    for i in range(1, n):
        if lr_list[i][0] > y:
            print(x, y)
            x = lr_list[i][0]
            y = lr_list[i][1]
        elif lr_list[i][1] > y:
            y = lr_list[i][1]
    print(x, y)
