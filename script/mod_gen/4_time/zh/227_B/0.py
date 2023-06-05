def f(a,b):
    return 4*a*b+3*a+3*b
N = int(input())
S = list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i+1,N):
        if S[i] == S[j]:
            ans += 1
        else:
            for a in range(1,1000):
                for b in range(a,1000):
                    if f(a,b) == S[i] and f(a,b) == S[j]:
                        ans += 1
print(N-ans)

if __name__ == '__main__':
    f()