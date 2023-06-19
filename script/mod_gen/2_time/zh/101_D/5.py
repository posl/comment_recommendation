def s(n):
    return sum([int(i) for i in str(n)])
K = int(input())
ans = []
for i in range(1, 200):
    for j in range(1, 200):
        ans.append(int(str(i) + '9' * j))
ans = sorted(ans)
print(*ans[:K], sep='\n')
