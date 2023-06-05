def main():
    N, S = map(int, input().split())
    cards = []
    for i in range(N):
        cards.append(list(map(int, input().split())))
    # print(cards)
    # 先计算正面和背面的和
    sum_front = 0
    sum_back = 0
    for i in range(N):
        sum_front += cards[i][0]
        sum_back += cards[i][1]
    # print(sum_front, sum_back)
    # 如果两个和都小于S，那么一定不可能
    if sum_front < S and sum_back < S:
        print("No")
        return
    # 如果两个和都大于S，那么一定不可能
    if sum_front > S and sum_back > S:
        print("No")
        return
    # 如果两个和中有一个等于S，那么一定可以
    if sum_front == S or sum_back == S:
        print("Yes")
        if sum_front == S:
            for i in range(N):
                print("H", end="")
        else:
            for i in range(N):
                print("T", end="")
        print("")
        return
    # 接下来就是sum_front < S and sum_back > S 或者 sum_front > S and sum_back < S
    # 那么就要分别考虑正面和背面的情况
    # sum_front < S and sum_back > S
    if sum_front < S and sum_back > S:
        # 正面的和肯定要小于S
        # 从大到小排列，先排正面
        cards.sort(key=lambda x: x[0], reverse=True)
        # print(cards)
        # 从大到小排列，再排背面
        cards.sort(key=lambda x: x[1], reverse=True)
        # print(cards)
        # 从前往后排列
        for i in range(N):
            if sum_front + cards[i][1] >= S:
                print("Yes")
                for j in range(i):
                    print("T", end="")
                print("H", end="")
                for j in range(i+1, N):
                    print("T", end="")
