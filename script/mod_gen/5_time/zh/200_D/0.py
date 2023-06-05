def find_2_sum(arr, target):
    dic = {}
    for i, a in enumerate(arr):
        if target - a in dic:
            return dic[target-a], i
        dic[a] = i
    return -1, -1

if __name__ == '__main__':
    find_2_sum()