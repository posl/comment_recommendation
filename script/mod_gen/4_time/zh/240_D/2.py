def solve():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] -= 1
            count += 1
    print(count)

if __name__ == '__main__':
    solve()