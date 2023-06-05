def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N-1):
        for j in range(i+1, N):
            if A[i-1] != A[j-1]:
                cnt += N-j
                break
    print(cnt)
    return
