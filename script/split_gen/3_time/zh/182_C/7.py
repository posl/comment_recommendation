def main():
    N = input()
    K = len(N)
    N = int(N)
    if N % 3 == 0:
        print(0)
        return
    for i in range(K):
        N = N // 10
        if N % 3 == 0:
            print(i + 1)
            return
    print(-1)
    return
