def main():
    # 读取数据
    N, M = map(int, input().split())
    A = [int(i)%M for i in input().split()]
    # 建立字典，记录每个数字出现的次数
    dic = {}
    for i in A:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    # 建立一个列表，记录每个数字出现的次数
    B = [0]*M
    for i in dic:
        B[i] = dic[i]
    # 开始计算
    sum = 0
    for i in range(M):
        if B[i] == 0:
            continue
        elif B[i] == 1:
            sum += i
        elif B[i] == 2:
            sum += i
            B[i] = 0
            B[(i+1)%M] += 1
        else:
            sum += (B[i]-2)*i
            B[i] = 2
            B[(i+1)%M] += 1
            B[(i+2)%M] += 1
    print(sum)

if __name__ == '__main__':
    main()