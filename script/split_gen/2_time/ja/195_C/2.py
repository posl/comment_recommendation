def main():
    N = int(input())
    ans = 0
    for i in range(len(str(N))):
        if i == 0:
            continue
        ans += (N - 10**i + 1) * i
    print(ans)
