def main():
    #输入
    N = int(input())
    A = list(map(int, input().split()))
    #处理
    #排序
    A.sort()
    #去重
    A = list(set(A))
    #去零
    A = [i for i in A if i != 0]
    #输出
    print(min([i for i in range(1, 2001) if i not in A]))
