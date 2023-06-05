def problem174_b():
    n, d = map(int, input().split())
    cnt = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x**2 + y**2 <= d**2:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    problem174_b()