def count_diff(s1, s2):
    diff_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff_count += 1
    return diff_count
s = input()
t = input()
min_diff = len(t)
for i in range(len(s) - len(t) + 1):
    diff_count = count_diff(s[i:i+len(t)], t)
    if diff_count < min_diff:
        min_diff = diff_count
print(min_diff)

if __name__ == '__main__':
    count_diff()