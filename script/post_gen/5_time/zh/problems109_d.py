Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    h,w=map(int,input().split())
    a=[]
    for i in range(h):
        a.append(list(map(int,input().split())))
    ans=[]
    for i in range(h):
        for j in range(w-1):
            if a[i][j]%2==1:
                a[i][j+1]+=1
                ans.append([i+1,j+1,i+1,j+2])
    for i in range(h-1):
        if a[i][w-1]%2==1:
            a[i+1][w-1]+=1
            ans.append([i+1,w,i+2,w])
    print(len(ans))
    for i in ans:
        print(*i)

=======
Suggestion 3

def get_even_num(H, W, a_list):
    even_num = 0
    for i in range(H):
        for j in range(W):
            if a_list[i][j] % 2 == 0:
                even_num += 1
    return even_num

=======
Suggestion 4

def check_even(matrix, h, w):
    count = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] % 2 == 0:
                count += 1
    return count

=======
Suggestion 5

def main():
    #输入
    H,W = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(H)]
    #处理
    ans = []
    for h in range(H):
        for w in range(W):
            if a[h][w]%2 == 1:
                if w != W-1:
                    a[h][w+1] += 1
                    ans.append([h+1,w+1,h+1,w+2])
                elif h != H-1:
                    a[h+1][w] += 1
                    ans.append([h+1,w+1,h+2,w+1])
    #输出
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        if i % 2 == 0:
            for j in range(W):
                if a[i][j] % 2 == 1:
                    if j < W-1:
                        a[i][j+1] += 1
                        ans.append([i+1, j+1, i+1, j+2])
                    else:
                        if i < H-1:
                            a[i+1][j] += 1
                            ans.append([i+1, j+1, i+2, j+1])
        else:
            for j in range(W-1, -1, -1):
                if a[i][j] % 2 == 1:
                    if j > 0:
                        a[i][j-1] += 1
                        ans.append([i+1, j+1, i+1, j])
                    else:
                        if i < H-1:
                            a[i+1][j] += 1
                            ans.append([i+1, j+1, i+2, j+1])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])
