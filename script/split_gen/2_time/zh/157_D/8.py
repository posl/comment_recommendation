def main():
    #读取输入
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    #建立友谊关系图
    friends = [[] for _ in range(N)]
    for a, b in AB:
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    #建立阻隔关系图
    blocks = [[] for _ in range(N)]
    for c, d in CD:
        blocks[c-1].append(d-1)
        blocks[d-1].append(c-1)
    #候选好友列表
    candidates = [0]*N
    #遍历所有用户
    for i in range(N):
        #遍历所有用户的好友
        for j in friends[i]:
            #如果用户i和用户j之间不存在友谊关系
            if i not in friends[j]:
                #如果用户i和用户j之间不存在阻隔关系
                if i not in blocks[j]:
                    #如果用户i和用户j之间存在路径
                    if path(friends, i, j):
                        #用户j是用户i的候选好友
                        candidates[i] += 1
    #打印答案
    print(*candidates)
