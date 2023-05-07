def main():
    P = int(input())
    # 硬貨の種類
    coin = [1,2,6,24,120,720,5040,40320,362880,3628800]
    coin.reverse()
    ans = 0
    for i in range(len(coin)):
        if P >= coin[i]:
            ans += P // coin[i]
            P = P % coin[i]
    print(ans)
