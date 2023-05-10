def main():
    N,K,D = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] < D:
        print(-1)
        return
    if K == 1:
        print(D)
        return
    if K == 2:
        if a[-2] < D:
            print(-1)
            return
        else:
            print(a[-2] + a[-1])
            return
    if K == 3:
        if a[-3] < D:
            print(-1)
            return
        else:
            print(a[-3] + a[-2] + a[-1])
            return
    if K == 4:
        if a[-4] < D:
            print(-1)
            return
        else:
            print(a[-4] + a[-3] + a[-2] + a[-1])
            return
