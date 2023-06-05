def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 选手数
    num = 2 ** N
    # 选手和评分的对应关系
    players = {}
    for i in range(num):
        players[A[i]] = i + 1
    # 选手的评分排序
    A.sort()
    # 比赛结果
    results = []
    for i in range(num - 1):
        if players[A[i]] < players[A[i+1]]:
            results.append(players[A[i]])
        else:
            results.append(players[A[i+1]])
    # 比赛结果排序
    results.sort()
    # 打印输掉比赛的选手
    print(results[1])
