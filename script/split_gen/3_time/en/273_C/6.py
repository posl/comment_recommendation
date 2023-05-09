def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a_set = set(a)
    a_dict = {a[i]: i for i in range(n)}
    a_dict_sorted = sorted(a_dict.items(), key=lambda x: x[0])
    a_dict_sorted.append((float("inf
