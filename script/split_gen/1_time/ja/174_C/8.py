def main():
    K = int(input())
    #K = 999983
    num = 7
    for i in range(1, K+1):
        if num % K == 0:
            print(i)
            return
        num = (num * 10 + 7) % K
    print(-1)
