def main():
    #输入
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    #处理
    #A=[i-1 if i%2==0 else i for i in A]
    #print(A)
    #print(sum(A))
    #输出
    if sum(A)-N//2<=X:
        print('Yes')
    else:
        print('No')
