def swap_list(list_, start, end):
    list_ = list(list_)
    for i in range(start, (end+start)//2+1):
        list_[i], list_[end+start-i] = list_[end+start-i], list_[i]
    return list_
