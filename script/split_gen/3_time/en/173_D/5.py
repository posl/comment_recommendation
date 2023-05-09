def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    if N % 2 == 0:
        ans = sum(A) - 2 * min(A)
    print(ans)
