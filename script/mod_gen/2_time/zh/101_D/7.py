def S(n):
    return sum(map(int, str(n)))
K = int(input())
ans = []
for i in range(1, 10):
    ans.append(i)
    while len(ans) < K and ans[-1] < 10 ** 15:
        ans.append(ans[-1] * 10)
    if len(ans) == K:
        break
for i in range(1, 10):
    for j in range(1, 10):
        ans.append(i * 10 ** 10 + j)
        while len(ans) < K and ans[-1] < 10 ** 15:
            ans.append(ans[-1] * 10)
        if len(ans) == K:
            break
    if len(ans) == K:
        break
ans.sort()
for a in ans:
    print(a)

if __name__ == '__main__':
    S()