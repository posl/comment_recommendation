def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    ans = N * (N - 1) // 2
    print(ans)
