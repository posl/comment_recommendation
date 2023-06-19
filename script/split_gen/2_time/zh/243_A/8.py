def main():
    # 读取输入
    v, a, b, c = map(int, input().split())
    # 处理
    if v < a:
        print("F")
        return
    v -= a
    if v < b:
        print("M")
        return
    v -= b
    if v < c:
        print("T")
        return
    print("T")
