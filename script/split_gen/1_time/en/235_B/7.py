def main():
    N = int(input())
    H = [int(h) for h in input().split()]
    ans = H[0]
    for i in range(1, N):
        if H[i] >= ans:
            ans = H[i]
    print(ans)
