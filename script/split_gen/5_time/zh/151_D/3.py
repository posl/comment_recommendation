def count_dis(l):
    l = l.split('#')
    return max([len(i) for i in l])
h, w = map(int, input().split())
l = []
for i in range(h):
    l.append(input())
l = list(filter(lambda x: '#' not in x, l))
print(count_dis(''.join(l)) + len(l) - 1)
