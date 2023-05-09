def main():
    N = int(input())
    cnt = 0
    n = 1
    while n <= N:
        cnt += (N-n+1)
        n *= 1000
    print(cnt)
