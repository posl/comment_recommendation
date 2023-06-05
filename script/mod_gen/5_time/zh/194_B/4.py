def min_time(a_list, b_list):
    min_time = 10**10
    for i in range(len(a_list)):
        for j in range(len(b_list)):
            if i == j:
                time = a_list[i] + b_list[j]
            else:
                time = max(a_list[i], b_list[j])
            if time < min_time:
                min_time = time
    return min_time

if __name__ == '__main__':
    min_time()