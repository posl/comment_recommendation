def find_ways_to_choose_pair(k):
    return int(k/2) * int(k/2 + k%2)
k = int(input())
print(find_ways_to_choose_pair(k))
