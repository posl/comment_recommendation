def main():
    #读取输入
    a1, a2, a3, a4 = map(int, input().split())
    #计算结果
    result = 0
    #100分的问题最多可以举办 a1 次
    result += a1
    #200分的问题最多可以举办 min(a2, result) 次
    result += min(a2, result)
    #300分的问题最多可以举办 min(a3, result) 次
    result += min(a3, result)
    #400分的问题最多可以举办 min(a4, result) 次
    result += min(a4, result)
    #输出结果
    print(result)
