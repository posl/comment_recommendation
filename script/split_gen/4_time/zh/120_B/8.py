def solve():
    A, B, K = map(int, input().split())
    cnt = 0
    for i in range(1, 10000):
        if A % i == 0 and B % i == 0:
            cnt += 1
            if cnt == K:
                print(i)
                break
