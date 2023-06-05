def main():
    n = int(input())
    t = []
    k = []
    a = []
    for i in range(n):
        t_i, k_i, *a_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)
        a.append(a_i)
    #print(t)
    #print(k)
    #print(a)
    # 从第n-1个开始逆向遍历
    # 如果有前置步骤，就加上前置步骤的时间
    # 如果没有前置步骤，就直接加上自己的时间
    # 选出最大的时间
    # 重复这个过程
    # 直到第一个动作为止
    #print("t[0] = ", t[0])
    #print("k[0] = ", k[0])
    #print("a[0] = ", a[0])
    #print("len(a[0]) = ", len(a[0]))
    #print("a[0][0] = ", a[0][0])
    #print("a[0][1] = ", a[0][1])
    #print("a[0][2] = ", a[0][2])
    #print("a[0][3] = ", a[0][3])
    #print("a[0][4] = ", a[0][4])
    #print("a[0][5] = ", a[0][5])
    #print("a[0][6] = ", a[0][6])
    #print("a[0][7] = ", a[0][7])
    #print("a[0][8] = ", a[0][8])
    #print("a[0][9] = ", a[0][9])
    #print("a[0][10] = ", a[0][10])
    #print("t[1] = ", t[1])
    #print("k[1] = ", k[1])
    #print("a[1] = ", a[1])
    #print("len(a[1]) = ", len(a[1]))
    #print("a[1][0] = ", a[
