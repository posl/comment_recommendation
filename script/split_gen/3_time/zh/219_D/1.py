def main():
    print('start')
    n = 3
    x = 8
    y = 8
    a = [3, 2, 2]
    b = [4, 3, 1]
    print(n)
    print(x, y)
    print(a, b)
    ans = -1
    for i in range(n):
        for j in range(n):
            if a[i] + b[j] >= x + y:
                if ans == -1:
                    ans = i + j
                else:
                    ans = min(ans, i + j)
    print(ans)
