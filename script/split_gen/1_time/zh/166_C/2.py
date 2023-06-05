def get_input():
    n, m = map(int, input().split())
    h_list = list(map(int, input().split()))
    ab_list = []
    for i in range(m):
        ab_list.append(list(map(int, input().split())))
    return n, m, h_list, ab_list
