def check(a, p, q, r):
    for i in range(1, len(a)):
        for j in range(i+1, len(a)):
            for k in range(j+1, len(a)):
                for l in range(k+1, len(a)):
                    if sum(a[i:j]) == p and sum(a[j:k]) == q and sum(a[k:l]) == r:
                        return True
    return False
n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
