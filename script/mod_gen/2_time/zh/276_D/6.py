def get_min_permutation(n, p):
    q = []
    for i in range(n):
        q.append(p[i])
    for i in range(n):
        for j in range(n-1-i):
            if q[j] > q[j+1]:
                tmp = q[j]
                q[j] = q[j+1]
                q[j+1] = tmp
    return q
n = int(input())
p = list(map(int, input().split()))
q = get_min_permutation(n, p)
for i in range(n):
    if i == n-1:
        print(q[i])
    else:
        print(q[i], end=' ')

if __name__ == '__main__':
    get_min_permutation()