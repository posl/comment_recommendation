def main():
    N = int(input())
    V = list(map(int, input().split()))
    V.sort()
    ans = (V[0] + V[1]) / 2
    for i in range(2, N):
        ans = (ans + V[i]) / 2
    print(ans)
