def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 'YES'
    for i in range(N):
        if p[i] != i + 1:
            ans = 'NO'
    print(ans)
