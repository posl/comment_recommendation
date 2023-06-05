def main():
    # 读取输入
    a,b,w = map(int,input().split())
    # 由于题目要求输出最大最小，所以先把最小的橙子数量算出来
    min_num = w*1000//b
    # 由于题目要求输出最大最小，所以先把最大的橙子数量算出来
    max_num = w*1000//a
    # 如果最小的橙子数量乘以最小的重量大于总重量或者最大的橙子数量乘以最大的重量小于总重量，那么就不存在这样的橙子
    if min_num*a > w*1000 or max_num*b < w*1000:
        print("UNSATISFIABLE")
    else:
        print(min_num,max_num)

if __name__ == '__main__':
    main()