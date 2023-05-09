def solve():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N-2):
        if A[i] == A[i+2]:
            cnt += 1
    if cnt == 0:
        print(1)
    elif cnt == 1:
        print(1)
    else:
        print(2)
