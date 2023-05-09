def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
    else:
        n = 1
        while n % K != 0:
            n = n * 10 + 7
            n %= K
        print(len(str(n)))
