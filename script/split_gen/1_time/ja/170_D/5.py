def main():
    N = int(input())
    A = list(map(int,input().split()))
    cnt = 0
    for i in range(2,10**6+1):
        cnt_ = 0
        for j in range(N):
            if A[j] % i == 0:
                cnt_ += 1
        if cnt_ >= 2:
            cnt += 1
    print(cnt)
