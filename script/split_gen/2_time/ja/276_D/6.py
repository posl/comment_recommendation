def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 1:
                print(ans)
                return
        A = [a//2 for a in A]
        ans += 1
