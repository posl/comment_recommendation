def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [i-1 for i in A]
    # 1からの距離を計算
    dist = [0]
    now = 0
    for i in range(N):
        now = A[now]
        dist.append(now)
    # 1からの距離がループするまでの距離を計算
    loop = [0]
    now = 0
    for i in range(N):
        now = dist[now]
        loop.append(now)
        if now == 0:
            break
    # 1からの距離がループするまでの距離を計算
    loop = [0]
    now = 0
    for i in range(N):
        now = dist[now]
        loop.append(now)
        if now == 0:
            break
    # K回テレポートしたときの町を計算
    if K <= len(loop)-1:
        print(loop[K]+1)
    else:
        K -= len(loop)-1
        K %= len(loop)-1
        print(loop[K]+1)

if __name__ == '__main__':
    main()