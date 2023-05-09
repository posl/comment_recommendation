def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    a = 7 % K
    for i in range(1, K+1):
        if a == 0:
            print(i)
            return
        a = (a*10 + 7) % K
    print(-1)
