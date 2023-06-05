def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 计算答案
    answer = -1
    for i in range(a, b + 1):
        if i % c == 0:
            answer = i
            break
    # 输出
    print(answer)
