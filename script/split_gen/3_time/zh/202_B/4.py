def main():
    # 读入
    s = input()
    # 180度旋转
    s = s[::-1]
    # 0,1,6,8,9替换
    s = s.replace('0', 'x')
    s = s.replace('1', 'y')
    s = s.replace('6', 'z')
    s = s.replace('8', '6')
    s = s.replace('9', '8')
    s = s.replace('x', '1')
    s = s.replace('y', '0')
    s = s.replace('z', '9')
    # 读出
    print(s)
