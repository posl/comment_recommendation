def main():
    # 读取输入
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    # 计算
    min_score = m*n - sum(a)
    if min_score < 0:
        print(0)
    elif min_score <= k:
        print(min_score)
    else:
        print(-1)
