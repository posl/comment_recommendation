def main():
    N,M = map(int,input().split())
    #マスの距離を求める
    def distance(i,j):
        return ((i-1)**2+(j-1)**2)**(1/2)
    #距離がMの倍数かどうかを判定する
    def judge(i,j):
        if distance(i,j) % M == 0:
            return True
        else:
            return False
    #距離がMの倍数のマスを求める
    def judge_list():
        judge_list = []
        for i in range(1,N+1):
            for j in range(1,N+1):
                if judge(i,j):
                    judge_list.append([i,j])
        return judge_list
    #距離がMの倍数のマスを求める
    judge_list = judge_list()
    #距離がMの倍数のマスからの最短距離を求める
    #距離がMの倍数のマスからの最短距離を求める
    def judge_distance(i,j):
        min_distance = 100000
        for k in range(len(judge_list)):
            if min_distance > abs(i-judge_list[k][0])+abs(j-judge_list[k][1]):
                min_distance = abs(i-judge_list[k][0])+abs(j-judge_list[k][1])
        return min_distance
    #距離がMの倍数のマスからの最短距離を求める
    for i in range(1,N+1):
        for j in range(1,N+1):
            if judge(i,j):
                print(0,end=' ')
            else:
                print(judge_distance(i,j),end=' ')
        print()
