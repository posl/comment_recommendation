def main():
    #输入
    a,b,c = map(int, input().split())
    #处理
    for i in range(a,b+1):
        if i % c == 0:
            print(i)
            break
    else:
        print(-1)
