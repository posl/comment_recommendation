def main():
    # data load
    data = input().rstrip().split(" ")
    # data[0] = A
    # data[1] = B
    # data[2] = C
    # data[3] = D
    # data[4] = E
    # フルハウスの条件を満たすかどうかを判定する
    if data.count(data[0]) == 3 and data.count(data[1]) == 2:
        print("Yes")
    elif data.count(data[0]) == 2 and data.count(data[1]) == 3:
        print("Yes")
    else:
        print("No")
