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
