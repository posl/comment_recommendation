def main():
    # 读入数据
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    # 处理查询
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1]-1] = query[2]
        else:
            print(A[query[1]-1])
