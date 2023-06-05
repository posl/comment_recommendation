def get_max_num(ary):
    max_num = 0
    for i in range(len(ary)):
        tmp = 0
        for j in range(len(ary)):
            tmp = tmp * 10 + ary[i][j]
        if max_num < tmp:
            max_num = tmp
    return max_num

if __name__ == '__main__':
    get_max_num()