def main():
    #输入
    N,P = map(int,input().split())
    A = list(map(int,input().split()))
    #判断
    count = 0
    for i in range(N):
        if A[i] < P:
            count += 1
    print(count)
