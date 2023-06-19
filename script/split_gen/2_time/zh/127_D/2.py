def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    bc = []
    for i in range(m):
        bc.append(list(map(int,input().split())))
    bc.sort(key=lambda x:x[1],reverse=True)
    j = 0
    for i in range(n):
        if j < m:
            if bc[j][0] > 0:
                if a[i] < bc[j][1]:
                    a[i] = bc[j][1]
                    bc[j][0] -= 1
                else:
                    break
            else:
                j += 1
                i -= 1
        else:
            break
    print(sum(a))
