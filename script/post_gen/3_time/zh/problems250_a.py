Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    r, c = map(int, input().split())
    print((H-r+1)*(W-c+1))

=======
Suggestion 2

def problems250_a():
    H,W = map(int, input().split())
    R,C = map(int, input().split())
    print(4 if R in [1,H] and C in [1,W] else 3 if R in [1,H] or C in [1,W] else 2)

=======
Suggestion 3

def main():
    H, W = [int(i) for i in input().strip().split()]
    R, C = [int(i) for i in input().strip().split()]
    print((H-R+1)*(W-C+1))

=======
Suggestion 4

def main():
    h,w = map(int, input().split())
    r,c = map(int, input().split())
    print((h-r+1)*(w-c+1))

=======
Suggestion 5

def problem250_a():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    result = 0
    if r==1 or r==h or c==1 or c==w:
        result = 2
    else:
        result = 4
    print(result)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H-R+1)*(W-C+1))

=======
Suggestion 7

def calc(R, C, H, W):
    ans = 0
    # 上
    if R > 1:
        ans += 1
    # 下
    if R < H:
        ans += 1
    # 左
    if C > 1:
        ans += 1
    # 右
    if C < W:
        ans += 1
    return ans

=======
Suggestion 8

def main():
    # 读取输入
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    # 计算
    ans = (h - r + 1) * (w - c + 1)
    # 输出
    print(ans)

=======
Suggestion 9

def get_num():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    num = 0
    if H == 1 and W == 1:
        return 0
    elif H == 1:
        if C == 1 or C == W:
            return 1
        else:
            return 2
    elif W == 1:
        if R == 1 or R == H:
            return 1
        else:
            return 2
    else:
        if R == 1 or R == H:
            num += 1
        if C == 1 or C == W:
            num += 1
        return num + 2

print(get_num())
