def get_input():
    #input_str = input()
    input_str = "4 150"
    input_list = input_str.split()
    n = int(input_list[0])
    k = int(input_list[1])
    #input_str = input()
    input_str = "150 140 100 200"
    input_list = input_str.split()
    h_list = []
    for i in range(n):
        h_list.append(int(input_list[i]))
    return n, k, h_list
