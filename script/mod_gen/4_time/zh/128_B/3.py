def solve():
    n = int(input())
    data = []
    for i in range(n):
        s, p = input().split()
        data.append((s, int(p)))
    data.sort(key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(data[i][1])

if __name__ == '__main__':
    solve()