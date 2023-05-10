def main():
    # 標準入力受け取り
    input_line = input()
    N, M = map(int, input_line.split())
    #print(N, M)
    input_line = input()
    A, B = map(int, input_line.split())
    #print(A, B)
    # 入力を配列に格納
    A_list = []
    B_list = []
    A_list.append(A)
    B_list.append(B)
    for i in range(1, M):
        input_line = input()
        A, B = map(int, input_line.split())
        #print(A, B)
        A_list.append(A)
        B_list.append(B)
    #print(A_list)
    #print(B_list)
    # 各橋を渡っている島の組み合わせを配列に格納
    bridge_list = []
    for i in range(M):
        bridge_list.append([A_list[i],B_list[i]])
    #print(bridge_list)
    # 2つの島の組み合わせを配列に格納
    island_list = []
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            island_list.append([i,j])
    #print(island_list)
    # 2つの島の組み合わせの組み合わせを配列に格納
    combination_list = []
    for i in range(len(island_list)):
        for j in range(i+1, len(island_list)):
            combination_list.append([island_list[i],island_list[j]])
    #print(combination_list)
    # 2つの島の組み合わせの組み合わせの組み合わせを配列に格納
    combination_list2 = []
    for i in range(len(combination_list)):
        for j in range(i+1, len(combination_list)):
            combination_list2.append([combination_list[i],combination_list[j]])
    #print(combination_list2)
    # 2つの島の組み合わせの組み合わせの組み合わせの組み合
