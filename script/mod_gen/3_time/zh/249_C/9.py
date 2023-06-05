def get_all_subsets(ss):
    return get_all_subsets_recur([], sorted(ss))

if __name__ == '__main__':
    get_all_subsets()