def main():
    K = int(input())
    n = 0
    for i in range(1, K+1):
        n = n*10 + 7
        n = n % K
        if n == 0:
            print(i)
            return
    print(-1)
