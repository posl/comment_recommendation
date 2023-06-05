def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    min_num = 10**9
    for i in range(n):
        if arr[i] < 0:
            cnt += 1
        arr[i] = abs(arr[i])
        min_num = min(min_num, arr[i])
    if cnt % 2 == 0:
        print(sum(arr))
    else:
        print(sum(arr) - 2 * min_num)

if __name__ == '__main__':
    solve()