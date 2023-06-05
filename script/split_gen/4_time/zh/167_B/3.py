def main():
    #读取输入
    A, B, C, K = map(int, input().split())
    #最大可能的和
    sum = 0
    #先从A中取出K张
    if A >= K:
        sum += K
        K = 0
    else:
        sum += A
        K -= A
    #再从B中取出K张
    if B >= K:
        K = 0
    else:
        K -= B
    #最后从C中取出K张
    if C >= K:
        sum -= K
    else:
        sum -= C
    #打印结果
    print(sum)
