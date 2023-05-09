def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a = list(set(a))
    a.sort()
    if len(a) == 1:
        print(n)
        return
    ans = [0] * n
    for i in range(len(a) - 1):
        ans[i] = n - (len(a) - i)
    ans[len(a) - 1] = 1
    print('
'.join(map(str, ans)))

if __name__ == '__main__':
    solve()