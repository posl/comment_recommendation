def main():
    N = int(input())
    ans = 0
    for i in range(0, len(str(N))):
        if N // (10 ** (3 * i)) == 0:
            break
        ans += (N // (10 ** (3 * i))) - 1
    print(ans)
