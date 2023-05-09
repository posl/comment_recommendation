def solve():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a.sort()
    max_value = a[-1]
    for i in range(n):
        if a[i] == max_value:
            print(a[-2])
        else:
            print(max_value)

if __name__ == '__main__':
    solve()