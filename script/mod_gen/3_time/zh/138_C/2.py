def get_final_value(list):
    if len(list) == 1:
        return list[0]
    else:
        new_list = []
        for i in range(len(list)-1):
            new_list.append((list[i] + list[i+1])/2)
        return get_final_value(new_list)

if __name__ == '__main__':
    get_final_value()