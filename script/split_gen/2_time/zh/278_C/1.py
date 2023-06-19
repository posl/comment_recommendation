def main():
    N, Q = map(int, input().split())
    # print(N, Q)
    # print(type(N), type(Q))
    # 1. 创建一个字典，key是用户，value是关注用户的列表
    user_follow = {}
    for i in range(1, N+1):
        user_follow[i] = []
    # 2. 根据输入的操作，更新字典
    for i in range(Q):
        t, a, b = map(int, input().split())
        # print(t, a, b)
        if t == 1:
            user_follow[a].append(b)
        elif t == 2:
            user_follow[a].remove(b)
        elif t == 3:
            if b in user_follow[a] and a in user_follow[b]:
                print("Yes")
            else:
                print("No")
