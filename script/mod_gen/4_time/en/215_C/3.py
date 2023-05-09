def solve():
    from itertools import permutations
    s, k = input().split()
    k = int(k)
    perms = sorted(set(permutations(s)))
    print(''.join(perms[k-1]))

if __name__ == '__main__':
    solve()