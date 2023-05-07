def main():
    import itertools
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    # 全ての経路の長さの合計を求める
    ans = 0
    for p in itertools.permutations(range(N)):
        for i in range(N-1):
            ans += ((xy[p[i]][0]-xy[p[i+1]][0])**2+(xy[p[i]][1]-xy[p[i+1]][1])**2)**0.5
    # N!で割る
    ans /= math.factorial(N)
    print(ans)

if __name__ == '__main__':
    main()