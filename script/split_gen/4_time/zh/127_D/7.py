def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    bc = [list(map(int,input().split())) for _ in range(m)]
    a.sort()
    bc.sort(key=lambda x:x[1],reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < bc[j][1]:
            a[i] = bc[j][1]
            bc[j][0] -= 1
            if bc[j][0] == 0:
                j += 1
            i += 1
        else:
            break
    print(sum(a))
