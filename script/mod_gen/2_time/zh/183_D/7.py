def main():
    n,w = map(int, input().split())
    stp = [list(map(int, input().split())) for _ in range(n)]
    #print(stp)
    # 1.按照开始时间排序
    stp.sort(key=lambda x:x[0])
    #print(stp)
    # 2.按照结束时间排序
    stp.sort(key=lambda x:x[1])
    #print(stp)
    # 3.按照使用量排序
    stp.sort(key=lambda x:x[2], reverse=True)
    #print(stp)
    # 4.按照开始时间排序
    stp.sort(key=lambda x:x[0])
    #print(stp)
    # 5.开始遍历
    w0 = w
    for i in range(n):
        if w0 < stp[i][2]:
            print("No")
            return
        w0 -= stp[i][2]
    print("Yes")

if __name__ == '__main__':
    main()