def main():
    #输入
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    #计算
    #地点i的平均温度是T-H[i]*0.006摄氏度。
    #因此，宫殿应该建在地点i。
    #平均温度最接近A摄氏度的地方
    #打印应该建造宫殿的地方的索引。
    #保证该方案是唯一的。
    #输出
    #打印应该建造宫殿的地方的索引。
    #print(H)
    #print(T)
    #print(A)
    #print(N)
    #print(H[0])
    #print(T-H[0]*0.006)
    #print(abs(A-(T-H[0]*0.006)))
    #print(abs(A-(T-H[0]*0.006)) - abs(A-(T-H[1]*0.006)))
    #print(abs(A-(T-H[0]*0.006)) - abs(A-(T-H[2]*0.006)))
    #print(abs(A-(T-H[1]*0.006)) - abs(A-(T-H[2]*0.006)))
    #print(abs(A-(T-H[1]*0.006)) - abs(A-(T-H[0]*0.006)))
    #print(abs(A-(T-H[2]*0.006)) - abs(A-(T-H[0]*0.006)))
    #print(abs(A-(T-H[2]*0.006)) - abs(A-(T-H[1]*0.006)))
    #print(abs(A-(T-H[2]*0.006)) - abs(A-(T-H[2]*0.006)))
    #print(abs(A-(T-H[2]*0.006)) - abs(A-(T-H[1]*0.006)))
    #print(abs(A-(T-H[2]*0.006)) - abs(A-(T-H[0]*0.006)))
    #print(abs(A-(T-H[1]*0.006)) - abs(A-(T-H[0]*0.006)))
    #print(abs(A

if __name__ == '__main__':
    main()