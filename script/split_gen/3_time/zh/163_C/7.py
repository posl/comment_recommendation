def count_subordinates(n, id_list):
    subordinate_count = [0] * n
    for i in range(n-1):
        subordinate_count[id_list[i]-1] += 1
    for i in range(n-1):
        subordinate_count[i] += subordinate_count[i+1]
    return subordinate_count
