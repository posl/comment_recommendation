def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #Bの各要素の出現回数をカウント
    B_cnt = [0] * (N+1)
    for b in B:
        B_cnt[b] += 1
    #Cの各要素の出現回数をカウント
    C_cnt = [0] * (N+1)
    for c in C:
        C_cnt[c] += 1
    #Aに対して、Bの各要素の出現回数を掛け合わせる
    ans = 0
    for a in A:
        ans += B_cnt[a] * C_cnt[a]
    print(ans)
