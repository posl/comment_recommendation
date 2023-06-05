def solve():
    n,p,q,r = map(int, input().split())
    a = list(map(int, input().split()))
    max_a = max(a)
    min_a = min(a)
    if max_a == min_a:
        print('Yes')
        return
    if p == q == r:
        print('Yes')
        return
    if max_a == p and max_a == q and max_a == r:
        print('Yes')
        return
    if max_a == p and max_a == q and min_a == r:
        print('Yes')
        return
    if max_a == p and min_a == q and max_a == r:
        print('Yes')
        return
    if min_a == p and max_a == q and max_a == r:
        print('Yes')
        return
    if max_a == p and min_a == q and min_a == r:
        print('Yes')
        return
    if min_a == p and max_a == q and min_a == r:
        print('Yes')
        return
    if min_a == p and min_a == q and max_a == r:
        print('Yes')
        return
    if min_a == p and min_a == q and min_a == r:
        print('Yes')
        return
    print('No')
    return

if __name__ == '__main__':
    solve()