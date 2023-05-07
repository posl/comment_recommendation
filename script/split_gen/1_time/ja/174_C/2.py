def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
    else:
        n = 1
        while 7 % K != 0:
            n += 1
            7 %= K
            7 *= 10
            7 += 7
        print(n)
