def main():
    #读取输入
    n = int(input())
    s = [input() for i in range(n)]
    #去重
    s = list(set(s))
    #输出
