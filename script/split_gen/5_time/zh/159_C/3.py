def main():
    # 读取输入
    L = int(input())
    # 计算
    v = (L/3)**3 if L%3 == 0 else (L//3+1)*(L//3)*(L//3)
    # 输出结果
    print(v)
