def get_max_orange_count(orange_count_list):
    max_orange_count = 0
    for i in range(len(orange_count_list)):
        for j in range(i, len(orange_count_list)):
            for k in range(1, max(orange_count_list[i:j+1])+1):
                orange_count = 0
                for l in range(i, j+1):
                    if orange_count_list[l] >= k:
                        orange_count += k
                if orange_count > max_orange_count:
                    max_orange_count = orange_count
    return max_orange_count

if __name__ == '__main__':
    get_max_orange_count()