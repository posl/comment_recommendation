def get_next_permutation(perm):
    n = len(perm)
    i = n - 1
    while i > 0 and perm[i - 1] >= perm[i]:
        i -= 1
    if i <= 0:
        return []
    j = n - 1
    while perm[j] <= perm[i - 1]:
        j -= 1
    perm[i - 1], perm[j] = perm[j], perm[i - 1]
    perm[i : ] = perm[n - 1 : i - 1 : -1]
    return perm
n = int(input())
p = list(map(int, input().split()))
p = get_next_permutation(p)
print(" ".join(map(str, p)))

if __name__ == '__main__':
    get_next_permutation()