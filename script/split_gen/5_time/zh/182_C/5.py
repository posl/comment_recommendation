def main():
    N = input()
    N = int(N)
    # print(N)
    if N % 3 == 0:
        print(0)
        return
    else:
        k = len(str(N))
        for i in range(1, k):
            for j in range(k - i):
                if int(str(N)[j + i]) % 3 == 0:
                    print(i)
                    return
        print(-1)
        return
