def max_orange(orange_list):
    max_num = 0
    for i in range(len(orange_list)):
        for j in range(i,len(orange_list)):
            for k in range(1,orange_list[j]+1):
                if k > max_num and min(orange_list[i:j+1]) >= k:
                    max_num = k
    return max_num

if __name__ == '__main__':
    max_orange()