def main():
    # 读取输入
    line = input()
    # 用空格分隔输入的字符串
    line = line.split()
    # 将字符串转换为数值
    line = [int(x) for x in line]
    # 找出0
    for i in range(len(line)):
        if line[i] == 0:
            print(i+1)
            break
