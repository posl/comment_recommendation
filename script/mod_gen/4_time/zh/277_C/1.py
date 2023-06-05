def solve():
    #读取输入
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int,input().split())
    #按照梯子的最高层排序
    AB = sorted(zip(A,B),key=lambda x:x[1])
    #print(AB)
    #开始遍历梯子
    now = 0
    for a,b in AB:
        if now < a:
            now = b
    print(now)

if __name__ == '__main__':
    solve()