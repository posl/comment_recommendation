def main():
    N = int(input())
    ans = 0
    while N > 1:
        if N % 2 == 0:
            N = N // 2
            ans += 1
        else:
            N -= 1
            ans += 1
    print(ans)
