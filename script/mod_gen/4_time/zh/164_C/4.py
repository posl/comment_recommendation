def count_num():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    s_set = set(s)
    return len(s_set)
print(count_num())
