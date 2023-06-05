def main():
    # 读取输入
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    # 检查A和B之间的距离
    if b - a > k:
        print(":(")
        return
    # 检查A和C之间的距离
    if c - a > k:
        print(":(")
        return
    # 检查A和D之间的距离
    if d - a > k:
        print(":(")
        return
    # 检查A和E之间的距离
    if e - a > k:
        print(":(")
        return
    # 检查B和C之间的距离
    if c - b > k:
        print(":(")
        return
    # 检查B和D之间的距离
    if d - b > k:
        print(":(")
        return
    # 检查B和E之间的距离
    if e - b > k:
        print(":(")
        return
    # 检查C和D之间的距离
    if d - c > k:
        print(":(")
        return
    # 检查C和E之间的距离
    if e - c > k:
        print(":(")
        return
    # 检查D和E之间的距离
    if e - d > k:
        print(":(")
        return
    # 如果程序执行到这里，说明所有的天线都可以直接通信
    print("Yay!")
