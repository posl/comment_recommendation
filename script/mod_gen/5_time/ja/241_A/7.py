def solve():
    a = list(map(int, input().split()))
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

if __name__ == '__main__':
    solve()