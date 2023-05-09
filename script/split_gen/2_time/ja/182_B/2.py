def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(2, 1001):
        cnt = 0
        for j in range(N):
            if A[j] % i == 0:
                cnt += 1
        if cnt > ans:
            ans = cnt
            ans_i = i
    print(ans_i)
