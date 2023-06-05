def get_max_orange(orange_list):
    max_orange = 0
    for i in range(len(orange_list)):
        for j in range(i, len(orange_list)):
            for k in range(1, orange_list[j]+1):
                if max_orange < k * (j-i+1):
                    max_orange = k * (j-i+1)
    return max_orange

if __name__ == '__main__':
    get_max_orange()