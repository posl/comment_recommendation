def main():
    K = int(input())
    if K % 2 == 0:
        print(-1)
        return
    if K == 7:
        print(1)
        return
    if K == 1:
        print(7)
        return
    ans = 7
    for i in range(2, K):
        ans = ans * 10 + 7
        if ans % K == 0:
            print(i)
            return
    print(-1)
