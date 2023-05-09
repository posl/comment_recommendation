def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    #print(xy)
    #N!通りのパターンを作る
    import itertools
    pattern = list(itertools.permutations(range(N), N))
    #print(pattern)
    #パターンの長さを求める
    length = []
    for i in range(len(pattern)):
        l = 0
        for j in range(N-1):
            l += ((xy[pattern[i][j]][0]-xy[pattern[i][j+1]][0])**2+(xy[pattern[i][j]][1]-xy[pattern[i][j+1]][1])**2)**(1/2)
        length.append(l)
    #print(length)
    #平均を求める
    ave = sum(length)/len(pattern)
    print(ave)
