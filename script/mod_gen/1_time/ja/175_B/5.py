def check(a,b,c):
    if a != b and b != c and c != a:
        if a+b > c and b+c > a and c+a > b:
            return True
    return False
N = int(input())
L = list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if check(L[i],L[j],L[k]):
                ans += 1
print(ans)

if __name__ == '__main__':
    check()