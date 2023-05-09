def main():
    N = int(input())
    ans = 0
    for i in range(N):
        A, B = map(int, input().split())
        ans += (B - A + 1) * (A + B) // 2
    print(ans)
