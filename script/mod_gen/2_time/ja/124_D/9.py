def main():
    #入力
    n, k = map(int, input().split())
    s = input()
    #問題を解く
    result = 0
    #1. 0と1の連続した区間を数える
    #2. 0の区間を1つずつ変えていき、最大の区間の長さを数える
    #3. 1の区間の長さを数える
    #4. 3と2の和を取る
    #5. 1の区間の長さが1の場合は、2の値に1を足す
    #6. 5の値が答え
    #1. 0と1の連続した区間を数える
    s_list = []
    s_count = 0
    for i in range(n):
        if i == 0:
            s_count += 1
            continue
        if s[i] == s[i-1]:
            s_count += 1
        else:
            s_list.append(s_count)
            s_count = 1
    s_list.append(s_count)
    #print(s_list)
    #2. 0の区間を1つずつ変えていき、最大の区間の長さを数える
    s_list_len = len(s_list)
    s_0_max = 0
    for i in range(0, s_list_len, 2):
        s_0 = 0
        for j in range(k):
            if (i+2*j) > (s_list_len-1):
                break
            s_0 += s_list[i+2*j]
        s_0_max = max(s_0_max, s_0)
    #print(s_0_max)
    #3. 1の区間の長さを数える
    s_1 = 0
    for i in range(1, s_list_len, 2):
        s_1 += s_list[i]
    #print(s_1)
    #4. 3と2の和を取る
    result = s_1 + s_0_max
    #

if __name__ == '__main__':
    main()