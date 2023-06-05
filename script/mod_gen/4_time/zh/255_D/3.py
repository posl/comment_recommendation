def problem255_d():
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        tmp = 0
        for j in range(n):
            tmp += abs(a[j] - x[i])
        print(tmp)

if __name__ == '__main__':
    problem255_d()