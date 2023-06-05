Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(L, Q, queries):
    # 初始的木板长度
    length = L
    # 从左到右的切割位置
    left = 0
    # 从右到左的切割位置
    right = L
    # 从左到右的切割位置的列表
    left_list = [0, L]
    # 从右到左的切割位置的列表
    right_list = [0, L]
    # 标记

=======
Suggestion 2

def main():
    l, q = map(int, input().split())
    cut = [0] * q
    for i in range(q):
        cut[i] = list(map(int, input().split()))
    cut.sort(key=lambda x: x[1])
    mark = []
    for i in range(q):
        if cut[i][0] == 1:
            mark.append(cut[i][1])
        else:
            mark.remove(cut[i][1])
            if i == q - 1:
                print(l - mark[0])
            else:
                print(cut[i + 1][1] - cut[i - 1][1])

=======
Suggestion 3

def main():
    l,q = map(int,input().split())
    mark = [0] * (l+1)
    mark[1] = 1
    mark[l] = 1
    for i in range(q):
        c,x = map(int,input().split())
        mark[x] = 1
        if c == 1:
            for j in range(x+1,l+1):
                if mark[j] == 1:
                    print(j-x)
                    break
            for j in range(x-1,0,-1):
                if mark[j] == 1:
                    print(x-j)
                    break
        else:
            for j in range(x+1,l+1):
                if mark[j] == 1:
                    print(j-x)
                    break
            for j in range(x-1,0,-1):
                if mark[j] == 1:
                    print(x-j)
                    break

=======
Suggestion 4

def main():
    L, Q = map(int, input().split())
    mark = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            mark.append(x)
        else:
            mark.sort()
            index = mark.index(x)
            print(mark[index] - mark[index - 1])
    return

=======
Suggestion 5

def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            left = cut.index(x)
            print(cut[left+1] - cut[left])
    return

main()

=======
Suggestion 6

def main():
    L, Q = map(int, input().split())
    mark = [0] * (L+1)
    mark[0] = 1
    mark[L] = 1
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            mark[x] = 1
        else:
            left = 0
            right = L
            while left <= right:
                mid = (left + right) // 2
                if mark[mid] == 1:
                    right = mid - 1
                else:
                    left = mid + 1
            left = left - 1
            left2 = 0
            right2 = L
            while left2 <= right2:
                mid2 = (left2 + right2) // 2
                if mark[mid2] == 1:
                    left2 = mid2 + 1
                else:
                    right2 = mid2 - 1
            right2 = right2 + 1
            print(right2 - left)

=======
Suggestion 7

def main():
    L,Q = map(int,input().split())
    mark = [0 for i in range(L+1)]
    for i in range(Q):
        c,x = map(int,input().split())
        if c==1:
            mark[x] = 1
        else:
            if x==0:
                print(L)
                continue
            left = 0
            right = L
            for j in range(x,0,-1):
                if mark[j] == 1:
                    left = j
                    break
            for j in range(x,L+1):
                if mark[j] == 1:
                    right = j
                    break
            print(right-left)

=======
Suggestion 8

def main():
    L, Q = map(int, input().split())
    cuts = []
    for i in range(Q):
        cuts.append(list(map(int, input().split())))
    #print(cuts)
    #print(cuts[0][0])
    #print(cuts[0][1])
    #print(len(cuts))
    #print(cuts[1][0])
    #print(cuts[1][1])
    #print(cuts[2][0])
    #print(cuts[2][1])
    #print(cuts[3][0])
    #print(cuts[3][1])
    #print(cuts[4][0])
    #print(cuts[4][1])
    #print(cuts[5][0])
    #print(cuts[5][1])
    #print(cuts[6][0])
    #print(cuts[6][1])
    #print(cuts[7][0])
    #print(cuts[7][1])
    #print(cuts[8][0])
    #print(cuts[8][1])
    #print(cuts[9][0])
    #print(cuts[9][1])
    #print(cuts[10][0])
    #print(cuts[10][1])
    #print(cuts[11][0])
    #print(cuts[11][1])
    #print(cuts[12][0])
    #print(cuts[12][1])
    #print(cuts[13][0])
    #print(cuts[13][1])
    #print(cuts[14][0])
    #print(cuts[14][1])
    #print(cuts[15][0])
    #print(cuts[15][1])
    #print(cuts[16][0])
    #print(cuts[16][1])
    #print(cuts[17][0])
    #print(cuts[17][1])
    #print(cuts[18][0])
    #print(cuts[18][1])
    #print(cuts[19][0])
    #print(cuts[19][1])
    #print(cuts[20][0])
    #print(cuts[20][1])
    #print(cuts[21][0])
    #print(cuts[21][1])
    #print(cuts[22][0])

=======
Suggestion 9

def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            i = cut.index(x)
            print(cut[i] - cut[i - 1])

=======
Suggestion 10

def main():
    l,q = map(int,input().split())
    mark = [0 for i in range(l+1)]
    mark[0] = 1
    mark[l] = 1
    for i in range(q):
        c,x = map(int,input().split())
        if c == 1:
            mark[x] = 1
        else:
            for j in range(x,0,-1):
                if mark[j] == 1:
                    left = j
                    break
            for j in range(x,l+1):
                if mark[j] == 1:
                    right = j
                    break
            print(right-left)
main()
