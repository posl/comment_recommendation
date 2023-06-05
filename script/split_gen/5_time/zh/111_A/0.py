def main():
    #读取一个字符串
    n = input()
    #替换
    n = n.replace('1', 'a')
    n = n.replace('9', '1')
    n = n.replace('a', '9')
    #输出结果
    print(n)
