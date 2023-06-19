def solve():
    # n = int(input())
    # s = list(map(int, input().split()))
    n = 5
    s = [666, 777, 888, 777, 666]
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                count += 1
    print(count)

if __name__ == '__main__':
    solve()