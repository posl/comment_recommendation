def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    num = 0
    for i in range(1, K+1):
        num = (num * 10 + 7) % K
        if num == 0:
            print(i)
            return
    print(-1)
