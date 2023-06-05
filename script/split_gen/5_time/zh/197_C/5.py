def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 2**31
    for i in range(n):
        x = 0
        for j in range(i,n):
            x = x | a[j]
            y = 0
            for k in range(j+1,n):
                y = y ^ a[k]
            ans = min(ans,x^y)
    print(ans)
