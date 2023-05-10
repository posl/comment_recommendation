def problem280_b():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0] * n
    for i in range(n):
        a[i] = s[i] - sum(a[:i])
    print(*a)

if __name__ == '__main__':
    problem280_b()