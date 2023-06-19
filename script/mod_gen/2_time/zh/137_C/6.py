def get_key(s):
    s_list = list(s)
    s_list.sort()
    return ''.join(s_list)
N = int(input())
s_list = []
for i in range(N):
    s_list.append(input())
s_list.sort()
s_list.append('')
count = 0
key = ''
for i in range(N):
    if key == s_list[i]:
        count += 1
    else:
        key = get_key(s_list[i])
print(count)

if __name__ == '__main__':
    get_key()