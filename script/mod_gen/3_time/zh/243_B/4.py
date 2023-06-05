def solve1():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res1 = 0
    res2 = 0
    for i in range(n):
        if a[i] == b[i]:
            res1 += 1
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and i != j:
                res2 += 1
    print(res1)
    print(res2//2)

if __name__ == '__main__':
    solve1()