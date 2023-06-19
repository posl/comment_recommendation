Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    l, q = map(int, input().split())
    cuts = [0, l]
    for _ in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            idx = cuts.index(x)
            print(cuts[idx] - cuts[idx - 1])

=======
Suggestion 3

def main():
    L,Q = map(int,input().split()) # L:木板长度，Q:查询次数
    mark = [0 for i in range(L+1)] # 标记数组，mark[i]为1表示i处有标记，mark[i]为0表示i处没有标记
    for i in range(Q):
        c,x = map(int,input().split()) # c:查询类型，x:标记位置
        if c == 1:
            mark[x] = 1 # 标记位置x
        else:
            # 找到x左边最近的一个标记位置
            left = x
            while left > 0 and mark[left] == 0:
                left -= 1
            # 找到x右边最近的一个标记位置
            right = x
            while right < L and mark[right] == 0:
                right += 1
            # 打印长度
            print(right - left)

=======
Suggestion 4

def main():
    L, Q = map(int, input().split())
    cut = [0] * (Q + 1)
    for i in range(1, Q + 1):
        c, x = map(int, input().split())
        if c == 1:
            cut[i] = x
    cut[0] = 0
    cut[Q] = L
    cut.sort()
    for i in range(1, Q + 1):
        if cut[i] == 0:
            continue
        print(cut[i] - cut[i - 1])

=======
Suggestion 5

def main():
    L,Q = map(int,input().split())
    mark = [0]*L
    mark[0] = 1
    mark[-1] = 1
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            mark[x-1] = 1
        else:
            a = 0
            for j in range(x-1):
                if mark[j] == 1:
                    a = j+1
            b = 0
            for j in range(x-1,L-1):
                if mark[j] == 1:
                    b = j+1
                    break
            print(b-a)

=======
Suggestion 6

def main():
    L, Q = map(int, input().split())
    mark = [0] * (Q + 1)
    mark[0] = L
    mark[Q] = 0
    for i in range(1, Q + 1):
        c, x = map(int, input().split())
        if c == 1:
            mark[i] = x
        else:
            mark[i] = mark[x]
            print(mark[x] - mark[i - 1])

=======
Suggestion 7

def main():
    l,q = map(int,input().split())
    mark = [0 for i in range(q)]
    for i in range(q):
        mark[i] = list(map(int,input().split()))
    #print(mark)
    mark.sort(key=lambda x:x[1])
    #print(mark)
    mark.insert(0,[0,0])
    mark.append([0,l])
    #print(mark)
    mark1 = []
    mark2 = []
    for i in range(1,len(mark)-1):
        if mark[i][0] == 1:
            mark1.append(mark[i][1])
        else:
            mark2.append(mark[i][1])
    #print(mark1)
    #print(mark2)
    mark1.sort()
    mark2.sort()
    #print(mark1)
    #print(mark2)
    mark1.insert(0,0)
    mark1.append(l)
    mark2.insert(0,0)
    mark2.append(l)
    #print(mark1)
    #print(mark2)
    for i in range(1,len(mark1)):
        mark1[i] = mark1[i] - mark1[i-1]
    for i in range(1,len(mark2)):
        mark2[i] = mark2[i] - mark2[i-1]
    #print(mark1)
    #print(mark2)
    ans = 0
    for i in mark1:
        for j in mark2:
            if i == j:
                ans = i
                break
    print(ans)

=======
Suggestion 8

def main():
    L,Q = map(int,input().split())
    mark = [False for i in range(L+1)]
    mark[0] = True
    mark[L] = True
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            mark[x] = True
        else:
            for i in range(x):
                if mark[x-i] == True:
                    left = x-i
                    break
            for i in range(x,L+1):
                if mark[i] == True:
                    right = i
                    break
            print(right-left)

=======
Suggestion 9

def main():
    L,Q = map(int,input().split())
    a = []
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            a.append(x)
        else:
            a.append(x)
            a.sort()
            b = []
            for j in range(len(a)-1):
                b.append(a[j+1]-a[j])
            print(min(b))

=======
Suggestion 10

def main():
    L, Q = map(int, input().split())
    mark = [0] * (L + 1)
    mark[0] = 1
    mark[L] = 1
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            mark[x] = 1
        else:
            left = 0
            right = 0
            for i in range(x, L + 1):
                if mark[i] == 1:
                    right = i
                    break
            for i in range(x, -1, -1):
                if mark[i] == 1:
                    left = i
                    break
            print(right - left)
