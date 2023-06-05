def main():
    # 输入
    a, b, c, d = map(int, input().split())
    # 处理
    # 1. a > b * d
    # 2. a <= b * d
    if a > b * d:
        # 1. a > b * d
        ans = 0
    else:
        # 2. a <= b * d
        ans = -1
        # 2.1. b * d - a % b == 0
        if b * d - a % b == 0:
            # 2.1.1. b * d - a % b == 0
            ans = (b * d - a) // b * c
        else:
            # 2.1.2. b * d - a % b != 0
            ans = (b * d - a) // b * c + c
    # 输出
    print(ans)
