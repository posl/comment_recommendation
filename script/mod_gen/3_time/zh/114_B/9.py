def get_num(s):
    if len(s) == 3:
        return int(s)
    else:
        return int(s[0:3])
s = input()
min_diff = 1000
for i in range(len(s)-2):
    diff = abs(get_num(s[i:i+3]) - 753)
    if diff < min_diff:
        min_diff = diff
print(min_diff)

if __name__ == '__main__':
    get_num()