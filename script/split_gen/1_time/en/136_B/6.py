def main():
    N = int(input())
    ans = N//10*9 + max(0, N%10 - 9 + 1)
    print(ans)
