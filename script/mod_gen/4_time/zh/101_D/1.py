def s(n):
    return sum(map(int, str(n)))
K = int(input())
ans = []
i = 1
while len(ans) < K:
    if i % s(i) == 0:
        ans.append(i)
    i += 1
for i in ans:
    print(i)

if __name__ == '__main__':
    s()