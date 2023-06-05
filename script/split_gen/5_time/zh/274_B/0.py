def get_num(num):
    count = 0
    for i in range(len(num)):
        if num[i] == '#':
            count += 1
    return count
H, W = map(int, input().split())
num = []
for i in range(H):
    num.append(input())
for i in range(W):
    print(get_num([num[j][i] for j in range(H)]), end=' ')
print()
