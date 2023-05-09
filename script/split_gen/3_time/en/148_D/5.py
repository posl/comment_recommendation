def main():
    N = int(input())
    A = list(map(int,input().split()))
    a = [0]*N
    for i in range(N):
        a[A[i]-1] += 1
    ans = N
    for i in range(N):
        if a[i] == 0:
            ans = -1
            break
        else:
            ans -= a[i] - 1
    print(ans)
