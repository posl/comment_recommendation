def main():
    # 读入数据
    line = input()
    line = line.split()
    m = int(line[0])
    h = int(line[1])
    # 计算
    if h % m == 0:
        print("Yes")
    else:
        print("No")
