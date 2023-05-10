def solve():
    n = int(input())
    v = list(map(int, input().split()))
    count = 0
    for i in range(0, n, 2):
        if v[i] != v[i+1]:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()