def main():
    #print("start")
    #读取数据
    #第一行
    line = input()
    #print(line)
    line = line.split()
    #print(line)
    N = int(line[0])
    M = int(line[1])
    #print(N,M)
    #第二行到第M+1行
    line = input()
    #print(line)
    line = line.split()
    #print(line)
    A = []
    B = []
    for i in range(M):
        A.append(int(line[2*i]))
        B.append(int(line[2*i+1]))
    #print(A)
    #print(B)
    #第M+2行
    line = input()
    #print(line)
    line = line.split()
    #print(line)
    K = int(line[0])
    #print(K)
    #第M+3行到第M+K+2行
    line = input()
    #print(line)
    line = line.split()
    #print(line)
    C = []
    D = []
    for i in range(K):
        C.append(int(line[2*i]))
        D.append(int(line[2*i+1]))
    #print(C)
    #print(D)
    #数据读取完毕
    #print("end")
    #print("start")
    #计算
    #print(N,M,K)
    #print(A)
    #print(B)
    #print(C)
    #print(D)
    #计算满足条件的个数
    count = 0
    for i in range(K):
        #print(i)
        #print(C[i])
        #print(D[i])
        #print(A)
        #print(B)
        #print(C)
        #print(D)
        if C[i] in A and D[i] in B:
            count += 1
    #print(count)
    #计算
    #print("end")
    #输出
    print(count)
    return
