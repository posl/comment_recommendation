def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    # A[i]を200で割った余りを取得
    A = [A[i] % 200 for i in range(N)]
    
    # 余りが同じものが何個あるかを数える
    from collections import Counter
    C = Counter(A)
    
    # 余りが同じものが2個以上ある場合、それらを2つ選ぶ組み合わせの数を求める
    ans = 0
    for v in C.values():
        if v >= 2:
            ans += v * (v - 1) // 2
    
    print(ans)
