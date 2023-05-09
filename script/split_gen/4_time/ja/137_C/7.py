def get_count(s):
    count_list = [0] * 26
    for c in s:
        count_list[ord(c) - ord('a')] += 1
    return tuple(count_list)
N = int(input())
count_dict = {}
for _ in range(N):
    s = input()
    count = get_count(s)
    if count not in count_dict:
        count_dict[count] = 0
    count_dict[count] += 1
ans = 0
for count in count_dict.values():
    ans += count * (count - 1) // 2
print(ans)
