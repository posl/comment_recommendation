def sum_of_contiguous_subsequences(a_list, k):
    result = 0
    for i in range(len(a_list)):
        for j in range(i+1, len(a_list)+1):
            if sum(a_list[i:j]) >= k:
                result += 1
    return result

if __name__ == '__main__':
    sum_of_contiguous_subsequences()