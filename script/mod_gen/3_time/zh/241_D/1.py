def get_min_k(list, k):
    list.sort(reverse=True)
    return list[k-1]

if __name__ == '__main__':
    get_min_k()