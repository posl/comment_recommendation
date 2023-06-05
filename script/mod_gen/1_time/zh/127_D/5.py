def main():
    # 读入数据
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    bc = []
    for i in range(m):
        bc.append(list(map(int,input().split())))
    # 操作
    a.sort()
    bc.sort(key=lambda x:x[1],reverse=True)
    idx = 0
    for i in range(m):
        for j in range(bc[i][0]):
            if idx >= n:
                break
            if a[idx] < bc[i][1]:
                a[idx] = bc[i][1]
                idx += 1
            else:
                break
    # 答案
    print(sum(a))

if __name__ == '__main__':
    main()