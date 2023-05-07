def get_input():
    n = int(input())
    ab_list = []
    for _ in range(n):
        ab_list.append(list(map(int, input().split())))
    return n, ab_list
