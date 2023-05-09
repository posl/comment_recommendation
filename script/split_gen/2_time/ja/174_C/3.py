def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    x = 0
    for i in range(1, K + 1):
        x = x * 10 + 7
        x %= K
        if x == 0:
            print(i)
            return
