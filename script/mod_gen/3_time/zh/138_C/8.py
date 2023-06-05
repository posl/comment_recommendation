def get_value(v_list):
    if len(v_list) == 1:
        return v_list[0]
    else:
        new_list = []
        for i in range(len(v_list)-1):
            value = (v_list[i] + v_list[i+1])/2
            new_list.append(value)
        return get_value(new_list)

if __name__ == '__main__':
    get_value()