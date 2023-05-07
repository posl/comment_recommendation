def main():
    N = int(input())
    ans = 0
    if N % 2 == 0:
        ans = N
    else:
        ans = N * 2
    print(ans)
