def read_ints():
    return list(map(int, input().split()))
N, M = read_ints()
conditions = []
for _ in range(M):
    conditions.append(read_ints())
K = int(input())
people = []
for _ in range(K):
    people.append(read_ints())
ans = 0
for i in range(2 ** K):
    balls = [0] * N
    for j in range(K):
        if (i >> j) & 1:
            balls[people[j][0] - 1] += 1
        else:
            balls[people[j][1] - 1] += 1
    cnt = 0
    for a, b in conditions:
        if balls[a - 1] > 0 and balls[b - 1] > 0:
            cnt += 1
    ans = max(ans, cnt)
print(ans)

if __name__ == '__main__':
    read_ints()