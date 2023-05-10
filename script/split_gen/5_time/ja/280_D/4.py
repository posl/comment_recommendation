def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    r = 7
    for i in range(1, K):
        if r % K == 0:
            print(i)
            return
        r = (r * 10 + 7) % K
    print(-1)
