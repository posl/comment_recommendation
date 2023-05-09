def main():
    N, K = map(int, input().split())
    S = input()
    # 1. 連続した0の数を数える
    # 2. 1の数がKより小さい場合は、0の数＋1
    # 3. 1の数がKより大きい場合は、K*2+1
    # 4. 1の数がKと同じ場合は、K*2
    # 1
    zero_count = 0
    zero_count_list = []
    for i in range(N):
        if S[i] == '0':
            zero_count += 1
        else:
            if zero_count > 0:
                zero_count_list.append(zero_count)
                zero_count = 0
    if zero_count > 0:
        zero_count_list.append(zero_count)
    # 2
    if len(zero_count_list) <= K:
        print(sum(zero_count_list) + len(zero_count_list))
        return
    # 3
    if len(zero_count_list) > K:
        print(K*2 + 1)
        return
    # 4
    if len(zero_count_list) == K:
        print(K*2)
        return

if __name__ == '__main__':
    main()