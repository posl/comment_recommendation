def main():
    n, s = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 'No'
    for i in range(1<<n):
        sum = 0
        for j in range(n):
            if (i>>j)&1:
                sum += a[j][0]
            else:
                sum += a[j][1]
        if sum == s:
            ans = 'Yes'
            break
    print(ans)
    if ans == 'Yes':
        for j in range(n):
            if (i>>j)&1:
                print('T', end='')
            else:
                print('H', end='')
        print()
