def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
    else:
        a = 7 % K
        for i in range(1, K + 1):
            if a == 0:
                print(i)
                break
            a = (a * 10 + 7) % K
