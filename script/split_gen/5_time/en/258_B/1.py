def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input())))
    ans = -float('inf')
    for i in range(n):
        for j in range(n):
            for k in range(8):
                x = i
                y = j
                for l in range(n - 1):
                    if k & 1:
                        x += 1
                    else:
                        x -= 1
                    if k & 2:
                        y += 1
                    else:
                        y -= 1
                    if x < 0 or x >= n or y < 0 or y >= n:
                        break
                    ans = max(ans, int(''.join(map(str, a[x][y] for x, y in zip(range(i, x + 1), range(j, y + 1))))))
    print(ans)
