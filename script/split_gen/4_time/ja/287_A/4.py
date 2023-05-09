def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    if s.count('For') > n//2:
        print('Yes')
    else:
        print('No')
