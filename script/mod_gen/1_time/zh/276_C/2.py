def find_permutation(n, p):
    # find the largest i such that p[i] < p[i+1]
    for i in range(n-2, -1, -1):
        if p[i] < p[i+1]:
            break
    else:
        # p is the largest permutation
        return p[::-1]
    # find the largest j such that p[j] > p[i]
    for j in range(n-1, i, -1):
        if p[j] > p[i]:
            break
    # swap p[i] and p[j]
    p[i], p[j] = p[j], p[i]
    # reverse p[i+1:]
    return p[:i+1] + p[i+1:][::-1]
n = int(input())
p = list(map(int, input().split()))
q = find_permutation(n, p)
print(' '.join(map(str, q)))

if __name__ == '__main__':
    find_permutation()