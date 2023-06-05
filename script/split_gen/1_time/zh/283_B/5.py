def main():
    # 读取输入
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    # 依次处理查询
    for _ in range(q):
        query = list(map(int, input().split()))
        # 查询类型1
        if query[0] == 1:
            a[query[1] - 1] = query[2]
        # 查询类型2
        else:
            print(a[query[1] - 1])
