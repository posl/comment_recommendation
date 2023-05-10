def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = [a%360 for a in A]
    A.sort(reverse=True)
    A.append(A[0]+360)
    ans = 0
    for i in range(N):
        ans = max(ans, A[i]-A[i+1])
    print(ans)
