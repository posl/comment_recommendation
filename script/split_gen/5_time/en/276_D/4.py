def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        flag = True
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
                ans += 1
                flag = False
                break
        if flag:
            break
    print(ans)
