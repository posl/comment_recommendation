def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    cnt = 0
    while True:
        flag = True
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
                cnt += 1
                flag = False
        if flag:
            break
    print(cnt)
