def get_min_swaps(s):
    atcoder = "atcoder"
    min_swaps = 0
    for i in range(len(s)):
        if s[i] != atcoder[i]:
            min_swaps += 1
    return min_swaps

if __name__ == '__main__':
    get_min_swaps()