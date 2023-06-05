def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    # 1. 暴力解法
    # count = 0
    # for i in range(n):
    #     for j in range(n):
    #         if a[i] == b[c[j]-1]:
    #             count += 1
    # print(count)
    # 2. 优化
    # a_dic = {}
    # for i in range(n):
    #     a_dic[i+1] = a[i]
    # count = 0
    # for i in range(n):
    #     if a_dic[b[c[i]-1]] == b[c[i]-1]:
    #         count += 1
    # print(count)
    # 3. 优化
    c_dic = {}
    for i in range(n):
        c_dic[i+1] = c[i]
    count = 0
    for i in range(n):
        if a[b[c_dic[i+1]-1]-1] == b[c_dic[i+1]-1]:
            count += 1
    print(count)
