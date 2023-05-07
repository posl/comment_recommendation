def main():
    N = int(input())
    ans = 0
    for k in range(1, N+1):
        ans += k * (N//k) * ((N//k)+1) // 2
    print(ans)
