def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] //= 2
            cnt += 1
        while A[i] % 3 == 0:
            A[i] //= 3
            cnt += 1
    if len(set(A)) == 1:
        print(cnt)
    else:
        print(-1)
