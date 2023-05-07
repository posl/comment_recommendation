def main():
    N = int(input())
    As = list(map(int, input().split()))
    min_A = min(As)
    # N=1の時は0を出力
    if N == 1:
        print(0)
        return
    # min_Aが2の倍数でない時は-1を出力
    if min_A % 2 != 0:
        print(-1)
        return
    # Asの要素を2で割り続ける回数を数える
    count = 0
    while True:
        for i in range(N):
            if As[i] % 2 != 0:
                print(-1)
                return
            As[i] //= 2
        if min(As) == min_A:
            break
        count += 1
    print(count)
