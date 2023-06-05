def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 逆向きに処理する
    # 1からNまでの数字がそれぞれ何回出現するかを記録する
    cnt = [0] * (n + 1)
    for i in range(n):
        cnt[a[i]] += 1
    # 1からNまでの数字が何番目に出現するかを記録する
    pos = [0] * (n + 1)
    for i in range(1, n + 1):
        pos[i] = i
    # 出現回数が多い順に並べ替える
    for i in range(n):
        for j in range(1, n - i):
            if cnt[j] < cnt[j + 1]:
                cnt[j], cnt[j + 1] = cnt[j + 1], cnt[j]
                pos[j], pos[j + 1] = pos[j + 1], pos[j]
    # 出現回数が多い順に出力する
    for i in range(1, n + 1):
        print(pos[i], end=' ')
    print()
