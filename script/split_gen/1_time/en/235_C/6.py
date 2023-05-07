def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    ans = []
    for i in range(q):
        x,k = map(int,input().split())
        c = 0
        for j in range(n):
            if a[j] == x:
                c += 1
            if c == k:
                ans.append(j+1)
                break
        else:
            ans.append(-1)
    print('
'.join(map(str,ans)))
