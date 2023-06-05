def main():
    # 读取输入
    input = int(input())
    # 处理
    day = 1
    sum = 0
    while True:
        sum += day
        if sum >= input:
            break
        day += 1
    # 输出
    print(day)
