def main():
    #读入数据
    N = int(input())
    p = [int(i) for i in input().split()]
    #初始化
    ans = 0
    for i in range(N):
        if p[i] == (i-1)%N or p[i] == i or p[i] == (i+1)%N:
            ans += 1
    #输出
    print(ans)
