def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        if all([a == A[0] for a in A]):
            break
        for i in range(N):
            if A[i] % 3 == 0:
                A[i] //= 3
                ans += 1
                break
        else:
            for i in range(N):
                if A[i] % 2 == 0:
                    A[i] //= 2
                    ans += 1
                    break
            else:
                ans = -1
                break
    print(ans)
