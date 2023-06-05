def main():
    # 读入数据
    n, m = list(map(int, input().split()))
    s = input().split()
    t = input().split()
    # 生成一个字典，键为车站名，值为是否停靠
    t_dict = {}
    for i in range(m):
        t_dict[t[i]] = True
    for i in range(n):
        if s[i] in t_dict:
            print("Yes")
        else:
            print("No")
