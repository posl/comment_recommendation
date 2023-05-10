def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    s = 7
    for i in range(K):
        if s % K == 0:
            print(i + 1)
            return
        s = s * 10 + 7
        s %= K
    print(-1)
