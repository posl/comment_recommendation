def get_min_name(name_list, order_list):
    #print(name_list)
    #print(order_list)
    min_name = name_list[0]
    for name in name_list[1:]:
        #print(name)
        for i in range(len(min_name)):
            #print(i)
            if name[i] == min_name[i]:
                continue
            else:
                if order_list.index(name[i]) < order_list.index(min_name[i]):
                    min_name = name
                break
        if len(name) < len(min_name):
            min_name = name
    return min_name
