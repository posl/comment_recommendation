def search_pair(x_list):
    pair_list = []
    for i in range(len(x_list)):
        for j in range(len(x_list)):
            if x_list[i] < x_list[j]:
                pair_list.append([x_list[i], x_list[j]])
    return pair_list

if __name__ == '__main__':
    search_pair()