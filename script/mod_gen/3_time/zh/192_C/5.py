def g_1(x):
    #将x的十进制数字按降序重新排列而得到的整数
    x = str(x)
    x = sorted(x,reverse=True)
    x = ''.join(x)
    x = int(x)
    return x

if __name__ == '__main__':
    g_1()