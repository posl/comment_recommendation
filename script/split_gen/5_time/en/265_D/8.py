def main():
    n, p, q, r = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(n):
        a = A[i]
        if a > r:
            break
        for j in range(i+1,n):
            b = A[j]
            if b > r:
                break
            for k in range(j+1,n):
                c = A[k]
                if c > r:
                    break
                for l in range(k+1,n):
                    d = A[l]
                    if d > r:
                        break
                    if a+b+c == p and b+c+d == q and c+d+a == r:
                        print('Yes')
                        return
    print('No')
    return
