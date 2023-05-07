def main():
    S = input()
    K = int(input())
    S_len = len(S)
    S_list = list(S)
    #print(S_list)
    X_count = 0
    X_count_list = []
    X_count_list.append(0)
    for i in range(S_len):
        if S_list[i] == "X":
            X_count += 1
        else:
            X_count_list.append(X_count)
            X_count = 0
    X_count_list.append(X_count)
    #print(X_count_list)
    X_count_list_len = len(X_count_list)
    #print(X_count_list_len)
    X_count_list_sum = 0
    #print(X_count_list_sum)
    for i in range(X_count_list_len):
        if i == 0 or i == X_count_list_len - 1:
            X_count_list_sum += X_count_list[i]
        else:
            if X_count_list[i] <= K:
                X_count_list_sum += X_count_list[i]
                K -= X_count_list[i]
            else:
                X_count_list_sum += K
                K = 0
    #print(X_count_list_sum)
    print(X_count_list_sum)
