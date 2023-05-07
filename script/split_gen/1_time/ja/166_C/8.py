def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    
    # 各展望台の良い展望台の数をカウントするリスト
    count = [0] * N
    
    for i in range(M):
        # 道を結ぶ展望台の標高を比較
        if H[AB[i][0] - 1] > H[AB[i][1] - 1]:
            # 展望台1の方が標高が高い場合
            count[AB[i][1] - 1] += 1
        elif H[AB[i][0] - 1] < H[AB[i][1] - 1]:
            # 展望台2の方が標高が高い場合
            count[AB[i][0] - 1] += 1
    
    # 良い展望台の数
    ans = count.count(0)
    print(ans)
