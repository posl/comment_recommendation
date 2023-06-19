def main():
    n,m = map(int,input().split())
    a = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        a[i] = list(map(int,input().split()))
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            else:
                for k in range(1,len(a[i])):
                    if a[i][k] in a[j]:
                        break
                else:
                    print('No')
                    break
        else:
            continue
        break
    else:
        print('Yes')
