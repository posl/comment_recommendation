def get_all_combinations(n, m):
    if n == 1:
        return [[i] for i in range(1, m + 1)]
    else:
        return [[i] + comb for i in range(1, m + 1) for comb in get_all_combinations(n - 1, m) if i > comb[0]]
n, m = map(int, input().split())
for comb in get_all_combinations(n, m):
    print(*comb)

if __name__ == '__main__':
    get_all_combinations()