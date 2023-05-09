def main():
    N, K = map(int, input().split())
    color_list = list(map(int, input().split()))
    color_set = set(color_list)
    if len(color_set) <= K:
        print(len(color_set))
        return
    color_count = {}
    for i in range(K):
        if color_list[i] in color_count:
            color_count[color_list[i]] += 1
        else:
            color_count[color_list[i]] = 1
    max_num = len(color_count)
    for i in range(K, N):
        color_count[color_list[i - K]] -= 1
        if color_count[color_list[i - K]] == 0:
            del color_count[color_list[i - K]]
        if color_list[i] in color_count:
            color_count[color_list[i]] += 1
        else:
            color_count[color_list[i]] = 1
        max_num = max(max_num, len(color_count))
    print(max_num)
