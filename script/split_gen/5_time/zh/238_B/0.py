def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(A[0]+360)
    ans = 0
    for i in range(N):
        ans = max(ans, A[i+1]-A[i])
    print(360-ans)
