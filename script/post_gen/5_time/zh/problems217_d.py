Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    L, Q = map(int, input().split())
    cuts = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            idx = cuts.index(x)
            print(cuts[idx] - cuts[idx-1])

=======
Suggestion 2

def main():
    l,q = map(int,input().split())
    mark = [0] * (l+1)
    mark[1] = l
    for i in range(q):
        c,x = map(int,input().split())
        if c == 1:
            mark[x],mark[x+1] = x,mark[x]-x
        else:
            print(mark[x])

=======
Suggestion 3

def main():
    L, Q = map(int, input().split())
    mark = [0 for i in range(L+1)]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            mark[x] = 1
        else:
            left = 0
            right = L
            for j in range(x, -1, -1):
                if mark[j] == 1:
                    left = j
                    break
            for j in range(x, L+1):
                if mark[j] == 1:
                    right = j
                    break
            print(right-left)

=======
Suggestion 4

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

=======
Suggestion 5

def main():
    L,Q = map(int,input().split())
    mark = [0]*(L+1)
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            mark[x] = 1
        else:
            if mark[x] == 1:
                mark[x] = 0
                left = 0
                right = 0
                for j in range(x+1,L+1):
                    if mark[j] == 0:
                        right = j
                        break
                for j in range(x-1,-1,-1):
                    if mark[j] == 0:
                        left = j
                        break
                print(right-left)
            else:
                print(0)

=======
Suggestion 6

def main():
    L, Q = map(int, input().split())
    X = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            X.append(x)
        else:
            X.sort()
            for i in range(len(X)):
                if X[i] == x:
                    print(X[i + 1] - X[i - 1])
                    break

=======
Suggestion 7

def main():
    L,Q = map(int,input().split())
    cut_point = [0,L]
    for i in range(Q):
        c_i,x_i = map(int,input().split())
        if c_i == 1:
            cut_point.append(x_i)
        if c_i == 2:
            cut_point.sort()
            index = cut_point.index(x_i)
            print(cut_point[index+1]-cut_point[index-1])

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    L,Q = map(int,input().split())
    mark = [0] * L
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            mark[x-1] = 1
        else:
            if mark[x-1] == 1:
                mark[x-1] = 0
                print(L)
            else:
                for j in range(x-1,L):
                    if mark[j] == 1:
                        len = j - x + 1
                        print(len)
                        break
