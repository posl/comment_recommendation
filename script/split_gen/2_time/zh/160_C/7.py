def main():
    #读取输入
    K,N = map(int,input().split())
    A = list(map(int,input().split()))
    #计算最大距离
    max_distance = 0
    for i in range(N-1):
        max_distance = max(max_distance,A[i+1]-A[i])
    #计算最小距离
    min_distance = K - A[N-1] + A[0]
    for i in range(N-1):
        min_distance = min(min_distance,A[i+1]-A[i])
    #计算答案
    print(K - max_distance - min_distance)
