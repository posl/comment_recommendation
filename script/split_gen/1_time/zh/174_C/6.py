def main():
    K = int(input())
    n = 0
    for i in range(1, K+1):
        n = n*10 + 7
        if n%K == 0:
            print(i)
            exit()
    print(-1)
