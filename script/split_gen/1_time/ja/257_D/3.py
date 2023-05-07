def main():
    N = int(input())
    jump = []
    for i in range(N):
        x, y, p = map(int, input().split())
        jump.append((x, y, p))
    ans = 10 ** 9
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1, p1 = jump[i]
            x2, y2, p2 = jump[j]
            cost = 0
            for k in range(N):
                x3, y3, p3 = jump[k]
                if p1 * cost >= abs(x1 - x3) + abs(y1 - y3) and p2 * cost >= abs(x2 - x3) + abs(y2 - y3):
                    continue
                elif p1 * cost >= abs(x1 - x3) + abs(y1 - y3):
                    cost = (abs(x2 - x3) + abs(y2 - y3) + p2 - 1) // p2
                else:
                    cost = (abs(x1 - x3) + abs(y1 - y3) + p1 - 1) // p1
            ans = min(ans, cost)
    print(ans)
