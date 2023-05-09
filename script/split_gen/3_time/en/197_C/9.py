def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    if N == 1:
        print(A[0])
        return
    A.sort(reverse = True)
    #print(A)
    ans = 0
    for i in range(N):
        ans = ans | A[i]
    print(ans)
