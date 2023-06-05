def main():
    N = int(input())
    p = list(map(int, input().split()))
    p = [i - 1 for i in p]
    ans = 0
    for i in range(N):
        if p[i] == i:
            if i == 0:
                if p[-1] == N - 1:
                    ans += 1
            else:
                if p[i - 1] == i - 1:
                    ans += 1
    print(ans)
