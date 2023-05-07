def main():
    P = int(input())
    # 10! から 1! までの硬貨をリストに格納
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[-1] * i)
    #print(coins)
    ans = 0
    # 10! から 1! までの硬貨を使って、支払うことができる枚数を求める
    for i in range(10, 0, -1):
        ans += P // coins[i-1]
        P %= coins[i-1]
    print(ans)
