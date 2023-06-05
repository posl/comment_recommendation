def main():
    #输入
    L,Q = map(int, input().split())
    #初始长度为L的木材
    wood = [L]
    #标记列表
    mark = []
    #处理查询
    for i in range(Q):
        c,x = map(int, input().split())
        if c==1:
            #将标记插入到标记列表
            mark.append(x)
        else:
            #找到标记所在的位置
            pos = bisect.bisect(mark, x)
            #计算标记左边的长度
            left = mark[pos-1] if pos>0 else 0
            #计算标记右边的长度
            right = L-mark[pos] if pos<len(mark) else 0
            #将标记左边的长度和标记右边的长度插入到木材列表
            wood.append(left)
            wood.append(right)
            #删除标记
            del mark[pos]
            #排序木材列表
            wood.sort()
            #打印最长的木材长度
            print(wood[-1])

if __name__ == '__main__':
    main()