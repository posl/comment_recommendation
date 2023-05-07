def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    x = 7
    for i in range(K):
        if x % K == 0:
            print(i + 1)
            return
        x = x * 10 + 7
    print(-1)
    return
