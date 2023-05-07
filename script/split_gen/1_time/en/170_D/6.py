def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    if N == 1:
        print(1)
        return
    A.sort()
    ans = 0
    for i in range(N):
        if i == 0:
            if A[i] != A[i+1]:
                ans += 1
        elif i == N-1:
            if A[i] != A[i-1]:
                ans += 1
        else:
            if A[i] != A[i-1] and A[i] != A[i+1]:
                ans += 1
    print(ans)
main()
I used Python3. I got AC.
My code is O(NlogN). I think this is the fastest way.
I tried to solve this problem by using Sieve of Eratosthenes, but I got TLE.
I think it is because I cannot use the fact that A_j does not divide A_i.
I will try to solve this problem by using Sieve of Eratosthenes.
I solved this problem by using Sieve of Eratosthenes.
I got AC.
I think this is the fastest way.
