def main():
    #读取输入
    S,T = input().split()
    A,B = input().split()
    U = input()
    #处理输入
    if S == U:
        A = str(int(A) - 1)
    else:
        B = str(int(B) - 1)
    #输出结果
    print(A,B)
