def get_orange_num(A,B,W):
    min_num = -1
    max_num = -1
    for i in range(A,B+1):
        if i*1000//B == W:
            if min_num == -1:
                min_num = i
            max_num = i
        if i*1000//A == W:
            if max_num == -1:
                max_num = i
            min_num = i
    return min_num,max_num
