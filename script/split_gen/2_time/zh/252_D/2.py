def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = 0
    a = 0
    b = 0
    for i in range(N):
        if A[i] == A[i+1]:
            b += 1
        else:
            ans += b*(b+1)*(b-1)//6
            a += b*(b-1)//2
            b = 0
    for i in range(N):
        if A[i] == A[i+1]:
            b += 1
        else:
            ans -= b*(b+1)*(b-1)//6
            b = 0
    ans += a*(a-1)//2
    print(ans)
