def get_all_subsets(s):
    if len(s) == 0:
        return [[]]
    subsets = get_all_subsets(s[1:])
    return subsets + [[s[0]] + subset for subset in subsets]
