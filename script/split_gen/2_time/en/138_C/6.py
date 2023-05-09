def main():
    N = int(input())
    V = [int(x) for x in input().split()]
    V.sort()
    ans = V[0]
    for i in range(1, N):
        ans = (ans + V[i]) / 2
    print(ans)
