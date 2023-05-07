def main():
    n, k = map(int, input().split())
    t = [0]*n
    for i in range(n):
        t[i] = list(map(int, input().split()))
    #全ての経路を列挙
    all_path = []
    for i in range(2, n+1):
        all_path += list(itertools.permutations(range(1, n), i))
    #全ての経路の移動時間の合計を計算
    sum_time = []
    for path in all_path:
        time = 0
        time += t[0][path[0]]
        for i in range(n-2):
            time += t[path[i]][path[i+1]]
        time += t[path[-1]][0]
        sum_time.append(time)
    #移動時間の合計がkになる経路の数を出力
    print(sum_time.count(k))

if __name__ == '__main__':
    main()