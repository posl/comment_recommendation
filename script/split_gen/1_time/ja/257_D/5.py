def main():
    n = int(input())
    jump = []
    for i in range(n):
        x, y, p = map(int, input().split())
        jump.append([x, y, p])
    ans = 10**10
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            tmp = 0
            for k in range(n):
                if i == k:
                    continue
                if jump[k][2] * (abs(jump[i][0] - jump[k][0]) + abs(jump[i][1] - jump[k][1])) < abs(jump[i][0] - jump[j][0]) + abs(jump[i][1] - jump[j][1]):
                    tmp = 10**10
                    break
                tmp = max(tmp, (abs(jump[i][0] - jump[k][0]) + abs(jump[i][1] - jump[k][1]) - 1) // jump[k][2] + 1)
            ans = min(ans, tmp)
    print(ans)
