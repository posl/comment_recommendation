def main():
    # 读取输入
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))
    # 用字典记录每个糖果的数目
    candy_dict = {}
    for candy in candies:
        if candy not in candy_dict:
            candy_dict[candy] = 1
        else:
            candy_dict[candy] += 1
    # 用集合记录每个糖果的数目
    candy_set = set(candy_dict.values())
    # 如果有k个糖果，那么输出k
    if len(candy_set) == k:
        print(k)
        return
    # 如果有k个糖果以上，那么输出k
    if len(candy_set) > k:
        print(k)
        return
    # 如果有k个糖果以下，那么输出糖果的种类数
    print(len(candy_set))
