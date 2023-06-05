def get_second_highest_mountain_name():
    dict = {}
    n = int(input())
    for i in range(n):
        s, t = input().split()
        dict[s] = int(t)
    sorted_dict = sorted(dict.items(), key=lambda d: d[1], reverse=True)
    return sorted_dict[1][0]
print(get_second_highest_mountain_name())
