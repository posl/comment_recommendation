def chk_same_shape(n, m, list_ab, list_cd):
    if m == 0:
        return 'Yes'
    list_ab.sort()
    list_cd.sort()
    if list_ab == list_cd:
        return 'Yes'
    else:
        return 'No'
n, m = map(int, input().split())
list_ab = []
list_cd = []
for i in range(m):
    a, b = map(int, input().split())
    list_ab.append([a, b])
for i in range(m):
    c, d = map(int, input().split())
    list_cd.append([c, d])
print(chk_same_shape(n, m, list_ab, list_cd))

if __name__ == '__main__':
    chk_same_shape()