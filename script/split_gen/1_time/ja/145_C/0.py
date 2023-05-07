def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    #print(x, y)
    #print(N)
    # リストの要素を全て入れ替える
    import itertools
    l = list(itertools.permutations(range(N)))
    #print(l)
    # 距離を求める関数
    def distance(i, j):
        return ( (x[i]-x[j])**2 + (y[i]-y[j])**2 )**0.5
    # 距離の合計を求める
    sum = 0
    for i in l:
        for j in range(N-1):
            sum += distance(i[j], i[j+1])
    #print(sum)
    # 平均を求める
    average = sum / len(l)
    print(average)
