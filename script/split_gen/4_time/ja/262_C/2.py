def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            if min(A[i],A[j]) == i+1 and max(A[i],A[j]) == j+1:
                cnt += 1
    print(cnt)
