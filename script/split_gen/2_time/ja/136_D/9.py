def main():
    S = input()
    N = len(S)
    # N = 10**5
    # S = "R" * (N-1) + "L"
    # S = "RRLRL"
    # S = "RRLLLLRLRRLL"
    # S = "RRRLLRLLRRRLLLLL"
    # print(S)
    # 連続するRの数を数える
    # Lが来たら、左から順に1ずつ足していく
    # 連続するRの数が奇数なら、中央のマスには2人、それ以外には1人
    # 連続するRの数が偶数なら、全て1人
    # Rが来たら、右から順に1ずつ足していく
    # 連続するLの数が奇数なら、中央のマスには2人、それ以外には1人
    # 連続するLの数が偶数なら、全て1人
    # 連続するRの数を数える
    count = 0
    for i in range(N):
        if S[i] == "R":
            count += 1
        else:
            break
    # 連続するRの数が奇数なら、中央のマスには2人、それ以外には1人
    if count % 2 == 1:
        ans = [1] * (count // 2) + [2] + [1] * (count // 2)
    # 連続するRの数が偶数なら、全て1人
    else:
        ans = [1] * count
    # Rが来たら、右から順に1ずつ足していく
    for i in range(N-1, count-1, -1):
        if S[i] == "L":
            ans[i-count] += 1
        else:
            break
    # 連続するLの数を数える
    count = 0
    for i
