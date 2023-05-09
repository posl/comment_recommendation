def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    count = [0]*(N+1)
    for i in A:
        count[i] += 1
    ans = [0]*(N+1)
    for i in range(1,N+1):
        ans[i] = count[i]*(count[i]-1)//2
    for i in range(1,N+1):
        print(sum(ans)-ans[A[i-1]]+count[A[i-1]]-1)
